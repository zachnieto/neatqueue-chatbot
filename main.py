import datetime
import os

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

load_dotenv()

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage, PromptTemplate,
)

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
    "asking the same question in the <#868549627652214794> channel. "
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



@client.event
async def on_ready():
    print("Bot has logged in")
    # await find_training_data()
    activity = Activity(type=ActivityType.watching, name=f"over the support channel")
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
    response = await query_engine.aquery(message.content)
    await message.reply(
        response.response,
        components=[
            Button(emoji="🗑️", custom_id="deletemessage", style=ButtonStyle.red)
        ],
    )
    print(
        f"Responded to '{message.content}' from {message.author} with '{response.response}'"
    )


@client.message_command(
    name="Answer With AI", default_member_permissions=Permissions(manage_channels=True)
)
async def answer_with_ai(inter: MessageCommandInteraction):
    await inter.send("Answering...", ephemeral=True)
    response = await query_engine.aquery(inter.target.content)
    await inter.target.reply(
        response.response,
        components=[
            Button(emoji="🗑️", custom_id="deletemessage", style=ButtonStyle.red)
        ],
    )


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

    async for message in support_channel.history(limit=None, oldest_first=False):
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
