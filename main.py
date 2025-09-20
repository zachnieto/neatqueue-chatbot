import datetime
import os
from collections import deque

from disnake import (
    Intents,
    Message,
    Permissions,
    MessageCommandInteraction,
    Status,
    Activity,
    ActivityType,
    ButtonStyle,
    MessageInteraction,
)
from disnake.ext import commands
from disnake.ext.commands import Bot
from disnake.ui import Button
from dotenv import load_dotenv
from llama_index.core.prompts import PromptType

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage, PromptTemplate,
)
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI

load_dotenv()

intents = Intents.default()
intents.message_content = True
intents.members = True

client = Bot(
    command_prefix=commands.when_mentioned,
    intents=intents,
)

if not os.path.exists("./storage"):
    print("Creating index")
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist()
else:
    print("Loading index")
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)

print("Loaded index")

Settings.llm = OpenAI(model="gpt-5-mini")

prompt_template_str = (
    "Context information from multiple sources is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "You are a tech support specialist for a Discord bot."
    "Given the information from multiple sources and not prior knowledge, "
    "answer the query. Be professional and as helpful as possible. "
    "Do not cite the source where your answer comes from. "
    "If you suggest using a command, format the command like `/command`. "
    "Always prioritize answers from the README.md file, which is the main source of information. "
    "Any command suggested must be found in the README.md file source. "
    "If the answer is not somewhat found in the given sources, then say you do not have that information, and suggest "
    "asking the same question in the <#1173046426255773707> channel. "
    "Only answer questions if you know the answer.\n"
    "Query: {query_str}\n"
    "Answer: "
)
prompt_template = PromptTemplate(
    prompt_template_str, prompt_type=PromptType.SUMMARY
)

query_engine = index.as_query_engine(
    text_qa_template=prompt_template
)



# ---------------- Conversation History ----------------
MAX_HISTORY_TURNS = int(os.getenv("CHAT_HISTORY_TURNS", "8"))
SEED_HISTORY_MESSAGES = int(os.getenv("CHAT_HISTORY_SEED", "12"))

# channel_id -> deque[(role, content)], where role in {"User", "Assistant"}
channel_histories = {}


def _get_history(channel_id: int):
    if channel_id not in channel_histories:
        channel_histories[channel_id] = deque(maxlen=MAX_HISTORY_TURNS * 2)
    return channel_histories[channel_id]


async def ensure_channel_history_initialized(channel):
    """Seed per-channel history from the most recent messages if empty."""
    history = _get_history(channel.id)
    if len(history) > 0:
        return

    try:
        # oldest_first=True so we append in chronological order
        async for m in channel.history(limit=SEED_HISTORY_MESSAGES, oldest_first=True):
            if not isinstance(m, Message) or not m.content:
                continue
            role = "Assistant" if m.author.bot else "User"
            _append_message(channel.id, role, m.content)
    except Exception:
        # Fail open if we cannot read history (permissions, etc.)
        pass


def _append_message(channel_id: int, role: str, content: str):
    if not content:
        return
    history = _get_history(channel_id)
    # de-duplicate adjacent identical entries (common when seeding includes current msg)
    if len(history) > 0 and history[-1][0] == role and history[-1][1] == content:
        return
    history.append((role, content))


def _format_history(channel_id: int) -> str:
    history = _get_history(channel_id)
    if not history:
        return ""
    lines = []
    for role, content in history:
        lines.append(f"{role}: {content}")
    return "\n".join(lines)


def compose_query_with_history(channel_id: int, user_message: str) -> str:
    history_text = _format_history(channel_id)
    if history_text:
        return (
            "Conversation so far:\n" + history_text + "\n\n" +
            f"Current question: {user_message}"
        )
    return user_message


@client.event
async def on_ready():
    print("Bot has logged in")
    # await find_training_data()
    activity = Activity(type=ActivityType.watching, name="over the support channel")
    await client.change_presence(status=Status.online, activity=activity)
    pass


@client.event
async def on_message(message: Message):
    if (
        message.channel.id
        not in [1099475384778633217, 1131752660740083763, 1180038609206788137]
        or message.author.bot
    ):
        return

    print(f"Responding to {message.content} from {message.author}")

    async with message.channel.typing():
        # Seed history if needed and compose query with conversation
        await ensure_channel_history_initialized(message.channel)
        _append_message(message.channel.id, "User", message.content)
        composed = compose_query_with_history(message.channel.id, message.content)
        response = await query_engine.aquery(composed)
    await message.reply(
        response.response,
        components=[
            Button(emoji="🗑️", custom_id="deletemessage", style=ButtonStyle.red)
        ],
    )
    _append_message(message.channel.id, "Assistant", response.response)
    print(
        f"Responded to '{message.content}' from {message.author} with '{response.response}'"
    )


@client.message_command(
    name="Answer With AI", default_member_permissions=Permissions(manage_channels=True)
)
async def answer_with_ai(inter: MessageCommandInteraction):
    await inter.send("Answering...", ephemeral=True)
    await ensure_channel_history_initialized(inter.channel)
    _append_message(inter.channel.id, "User", inter.target.content)
    composed = compose_query_with_history(inter.channel.id, inter.target.content)
    response = await query_engine.aquery(composed)
    await inter.target.reply(
        response.response,
        components=[
            Button(emoji="🗑️", custom_id="deletemessage", style=ButtonStyle.red)
        ],
    )
    _append_message(inter.channel.id, "Assistant", response.response)


@client.event
async def on_button_click(inter: MessageInteraction):
    if inter.component.custom_id != "deletemessage":
        return

    await inter.response.defer(ephemeral=True)

    if not inter.author.guild_permissions.manage_messages:
        return await inter.send(
            "You do not have permissions to delete this!", ephemeral=True
        )

    await inter.delete_original_message()


async def find_training_data():
    print("Starting updating support data")
    support_channel = client.get_channel(868549627652214794)

    qa_data = []
    all_data = []

    date = datetime.datetime.fromtimestamp(0)

    for file in os.listdir("data"):
        if file.startswith("history-"):
            name = file.removeprefix("history-").removesuffix(".txt")
            date = datetime.datetime.strptime(name, "%Y-%m-%d")
            break

    date = date.replace(tzinfo=datetime.timezone.utc)

    async for message in support_channel.history(limit=None, oldest_first=False, after=date):
        if message.created_at < date:
            break

        if (
            not isinstance(message, Message)
            or not message.content
            or len(message.content) < 4
        ):
            continue

        print(f"Training off of: {message.content}")

        if (
            message.reference
            and message.reference.resolved
            and isinstance(message.reference.resolved, Message)
        ):
            qa_data.append(
                f"Question: {message.reference.resolved.content}\nAnswer: {message.content}\n\n"
            )
        all_data.append(message.content)

    for file in os.listdir("data"):
        if file.startswith("history") or file.startswith("qa"):
            os.remove(os.path.join("data", file))

    date_str = datetime.datetime.now().strftime("%Y-%m-%d")

    with open(f"data/qa-{date_str}.txt", "a", encoding="utf-8") as f:
        f.write("\n" + "\n".join(reversed(qa_data)))

    with open(f"data/history-{date_str}.txt", "a", encoding="utf-8") as f:
        f.write("\n" + "\n".join(reversed(all_data)))

    print("Finished updating support data")


if __name__ == "__main__":
    token = os.getenv("TOKEN")
    client.run(token)
