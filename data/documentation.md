# Quick start
Starting a queue is super simple with NeatQueue, just run one of the following commands:
- /setup for an interactive walk through
- /startqueue for a simple default configuration
- /load [config_id] for a specific queue configuration

# Premium Commands

## Language
### /language overrides set  
Toggle on/off using the custom overrides. Usage: /language overrides set [original_phrase] (overriden_phrase)  
- original_phrase: (Required) Existing phrase to override  
- overriden_phrase: (Optional) Replacement phrase, omit to go back to default  
Usage Permissions: Staff Role or Manage Channels Permission  

### /language overrides toggle  
Toggle on/off using the custom overrides. Usage: /language overrides toggle [toggle]  
- toggle: (Required) Toggle custom overrides. Options: Enabled, Disabled  
Usage Permissions: Staff Role or Manage Channels Permission  

### /language overrides upload  
Upload a custom overrides file. Usage: /language overrides upload [custom_overrides]  
- custom_overrides: (Required) Custom translation overrides, omit to remove  
The overrides file is JSON format, and can be found here: https://www.neatqueue.com/default_overrides.json The keys (left side) signify the already existing English phrase the bot uses. The value (right side) is the value that replaces the key. Sometimes an entry will include special charcters similar to {}. The total number of these signifiers in each entry must remain constant. If an override does not match the count of signifiers, it will not be used.  
Usage Permissions: Staff Role or Manage Channels Permission  

## Leaderboard Config  
Leaderboard titles are hyperlinks to the website version of the leaderboard.  

### /leaderboardconfig url  
Create a custom website url for leaderboards. Usage: /leaderboardconfig url [url]  
- url: (Required) Custom url for this channel's leaderboard  
Usage Permissions: Staff Role or Manage Channels Permission  

## Messages + Styling Premium  
### /message color  
Sets the color for all embeds and/or buttons in messages. Usage: /message color (color) (button_color)  
- color: (Optional) Either a color by name, or by HEX value (Ex: 00FF55)  
- button_color: (Optional) Button color name. Options: Blurple, Gray, Green, Red, Random  
Usage Permissions: Staff Role or Manage Channels Permission  

### /message queuemessage footer  
(Default: None) Set a footer for the queue message. Usage: /message queuemessage footer (text) (icon_url)  
- text: (Optional) Footer contents, or omit to remove  
- icon_url: (Optional)  
Usage Permissions: Staff Role or Manage Channels Permission  

### /message queuemessage image  
(Default: None) Set an image for the queue message. Usage: /message queuemessage image (image_url)  
- image_url: (Optional) Direct URL of image, or omit to remove  
Usage Permissions: Staff Role or Manage Channels Permission  

### /message queuemessage thumbnail  
(Default: None) Set a thumbnail for the queue message. Usage: /message queuemessage thumbnail (image_url)  
- image_url: (Optional) Direct URL of image, or omit to remove  
Usage Permissions: Staff Role or Manage Channels Permission

# User Commands
## Cancel
Start a vote to cancel the current match, usage: /cancel

## Compare
Compare your stats to the given player. Usage: /compare [player2] (player1) (hidden)
Arguments:
- player2: (Required) Enter the second user you want to compare to.
- player1: (Optional) Enter the first user you want to compare to, or omit for yourself.
- hidden: (Optional) If you want the stats to be hidden.

## Force Start
Start a vote to forcestart the game, skips vote if used by staff. Usage: /forcestart

## Leaderboard
Shows the leaderboard for the current queue's game. Usage: /leaderboard (page) (type) (queue_name)
Options: MMR, Peak MMR, Points, MVPs, Games, Wins, Losses, Winrate, Streak, Peak Streak
Arguments:
- page: (Optional) The desired page number.
- type: (Optional) The type of leaderboard to display.
- queue_name: (Optional) The queue name to view.

## Parties/Teams/Clans/Groups
- CAPTAIN ONLY: Cancel all pending invites. Usage: /party cancelinvites [party_name], Arguments: party_name: (Required) The party name.

- CAPTAIN ONLY: Designate a new captain if you are the current one. Usage: /party captain [player] [party_name], Arguments: player: (Required) The new captain. party_name: (Required) The team name.

- Create a new party. Usage: /party create [party_name]. Arguments: party_name: (Required) The party name.

- CAPTAIN ONLY: Disband a party. Usage: /party disband [party_name]. Arguments:party_name: (Required) The party name.

- CAPTAIN ONLY: Invite a new player to the party. Usage: /party invite [player] [party_name]. Arguments: player: (Required) Player to invite. party_name: (Required) The party name.

- Join a party. Usage: /party join [party_name]. Arguments: party_name: (Required) The party name.

- CAPTAIN ONLY: Kick a player from the party. Usage: /party kick [player] [party_name]. Arguments: player: (Required) The player to kick. party_name: (Required) The team name.

- Leave a party. Usage: /party leave [party_name]. Arguments: party_name: (Required) The party name.

- List your parties. Usage: /party list

- Specify your role in the party. Usage: /party selectrole [party_name] [role]. Arguments: party_name: (Required) The party name. role: (Required) Your role.

- View the specified party. Usage: /party view [party_name]. Arguments: party_name: (Required) The party name.

## Register
Initialize your MMR using your account of the game you specified (Not recommended at all). Usage: /register [account]
Arguments: account: (Required) Account details.

## Require IGN
Sets your IGN for this queue to help with easy lobby setup. Usage: /ign [ign]
Arguments: ign: (Required) Your IGN for this queue's platform.

## Roles
Set your role. Usage: /role (role)
Arguments: role: (Optional) Preferred role to use, or omit to remove.

## Stats
Shows your stats. Usage: /stats (hidden) (user) (all_time)
Arguments:
- hidden: (Optional) If you want the stats to be hidden.
- user: (Optional) The user you want to check stats of.
- all_time: (Optional) If you want to view all time stats, only applies to monthly queues.

## Substitute
Substitute yourself for the given player. Usage: /substitute [player]
Arguments: player: (Required) Enter the player to replace you.


# Admin commands

## AnonymousQueue / Hiding Names
Sets whether to hide the names of players in queue. Usage: /anonymousqueue [mode]
Usage Permissions: Staff Role or Manage Channels Permission
Arguments:
- mode: (Required) Hide players names in queue.
- Options: Enabled, Disabled

## Anti Cheat
Sets the anticheat channel to show flagged users.
Usage: /anticheat channel [channel]
Arguments:
- channel: (Required) The desired anticheat channel.

### /anticheat enable
Enable or disable the anticheat system. Usage: `/anticheat enable [toggle]`
Arguments:
* toggle: (Required) Toggle for anticheat.
  * Options: Enabled, Disabled

### /anticheat flag incorrectvoting
Set an anticheat trigger for players who vote for the wrong team. Usage: `/anticheat flag incorrectvoting [toggle]`
Arguments:
* toggle: (Required) Flag users who vote wrong.
  * Options: Enabled, Disabled

### /anticheat flag newaccount
Set an anticheat trigger for new accounts. Usage: `/anticheat flag newaccount [age]`
Arguments:
* age: (Required) Account age in days.

### /anticheat flag rejoins
Set an anticheat trigger for if a player rejoins a server. Usage: `/anticheat flag rejoins [toggle]`
Arguments:
* toggle: (Required) Flag users who rejoin the server if they already have stats.
  * Options: Enabled, Disabled

### /anticheat flag streak
Set an anticheat trigger for a player's streak. Usage: `/anticheat flag streak [streak]`
Arguments:
* streak: (Required) Streak to trigger a flag.

### /anticheat role
Set a role to assign to flagged players. Usage: `/anticheat role [role]`
Arguments:
* role: (Required) Role to assign.

Note: All commands require Staff Role or Manage Channels Permission.

## Auto Ping
Auto ping commands

- Remove the set auto ping rule. Usage: /autoping remove. Usage Permissions: Staff Role or Manage Channels Permission

- Automatically ping the given role when the queue hits the given size. Usage: /autoping set [role] [size] (delete_after). Usage Permissions: Staff Role or Manage Channels Permission
Arguments:
- role: (Required) Role to ping.
- size: (Required) Ping when the queue hits this size.
- delete_after: (Optional) Delete the ping after this many seconds.

## Balance By

### /balanceby roles
Order of role to skill from lowest to highest rated, used if balance by ROLES is set trough /balanceby type, not MMR.
Usage: /balanceby roles (role1) (role2) (role3) (role4) (role5) (role6) (role7) (role8) (role9) (role10)
Arguments:
- role1: (Optional) The role to use in balancing.
- role2: (Optional) The role to use in balancing.
- role3: (Optional) The role to use in balancing.
- role4: (Optional) The role to use in balancing.
- role5: (Optional) The role to use in balancing.
- role6: (Optional) The role to use in balancing.
- role7: (Optional) The role to use in balancing.
- role8: (Optional) The role to use in balancing.
- role9: (Optional) The role to use in balancing.
- role10: (Optional) The role to use in balancing.
Usage Permissions: Staff Role or Manage Channels Permission

### /balanceby type
(Default: mmr) Sets how teams are balanced.
Usage: /balanceby type [mode]
Arguments:
- mode: (Required) How teams are balanced.
    Options: Roles, MMR
Usage Permissions: Staff Role or Manage Channels Permission

## Best Of
Sets whether the queue is a best of 3, 5, 7, etc.
Usage: /bestof [number] (vote) (voteselection) (eligible_voters)
Arguments:
- number: (Required) Best of number.
- vote: (Optional) Whether players can vote on the number of matches to play.
- voteselection: (Optional) Whether to pick the majority vote, or the lowest voted number. Options: Majority, Lowest
- eligible_voters: (Optional) Who on the team can vote. Defaults to All if no captain selected. Options: All, Captains
Usage Permissions: Staff Role or Manage Channels Permission

## Captain Selection
### /captains automute
Automatically mute all non-captains during selection to remove bias.
Usage: /captains automute [toggle]
Arguments:
- toggle: (Required) If players are muted. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /captains bannedrole
Sets a role which is banned from being captain.
Usage: /captains bannedrole (role)
Arguments:
- role: (Optional) The banned role.
Usage Permissions: Staff Role or Manage Channels Permission

### /captains drafttype
Sets the type of draft to either Snake or Straight.
Usage: /captains drafttype [type]
Arguments:
- type: (Required) The type of draft to use. Options: Snake (1-2-2-2), Straight (1-1-1-1), Hybrid (1-1/2-1-1), Hybrid 2 (1-2-1-1), Vote
Usage Permissions: Staff Role or Manage Channels Permission

### /captains firstpick
Specify who gets the first pick in captain selection.
Usage: /captains firstpick [mode]
Arguments:
- mode: (Required) Who gets the first pick. Options: Highest Rated, Lowest Rated, Random
Usage Permissions: Staff Role or Manage Channels Permission

### /captains reshuffle
Sets whether players can reshuffle captains in random captain selection.
Usage: /captains reshuffle [toggle]
Arguments:
- toggle: (Required) Whether reshuffling is enabled or disabled. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /captains role
Sets a role which gets priority for being captain.
Usage: /captains role (role)
Arguments:
- role: (Optional) The captain role.
Usage Permissions: Staff Role or Manage Channels Permission

### /captains selection
Choose how captains will be picked.
Usage: /captains selection
Usage Permissions: Staff Role or Manage Channels Permission

## Channel Config
Due to Discord API limitations, NeatQueue can only update the channel name twice per a 10 minute period.

### /channel category
(Default: Parent) Sets whether created channels go in a separate or the parent category.
Usage Permissions: Staff Role or Manage Channels Permission
Usage: /channel category [category_mode] (category)
Arguments:
- category_mode: (Required) The category setting. If mode is Specified, you must provide the category. Options: Parent, New, Specified
- category: (Optional) The specific category if category_mode is Specified.

### /channel name queueempty
Set the channel name when a queue is empty. Can only be updated twice per 10 minutes!.
Usage: /channel name queueempty [channel_name]
Arguments:
- channel_name: (Required) The channel name.
Usage Permissions: Staff Role or Manage Channels Permission

### /channel name queuelocked
Set the channel name when a queue is locked. Can only be updated twice per 10 minutes!.
Usage: /channel name queuelocked [channel_name]
Arguments:
- channel_name: (Required) The channel name.
Usage Permissions: Staff Role or Manage Channels Permission

### /channel name queuenotempty
Set the channel name when a queue isn't empty. Can only be updated twice per 10 minutes!.
Usage: /channel name queuenotempty [channel_name]
Arguments:
- channel_name: (Required) The channel name.
Usage Permissions: Staff Role or Manage Channels Permission

### /channel restrictions
(Default: enabled) Sets whether created channels have restrictions.
Usage: /channel restrictions [mode]
Arguments:
- mode: (Required) If channels are restricted. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

## Clear Queue
Clears the running queue. Usage: /clearqueue
Usage Permissions: Staff Role or Manage Channels Permission

## Command Button
(BETA) Sends a button which triggers a command when clicked. Usage: /commandbutton create [command] (color) (emoji) (label)
Arguments:
- command: (Required) Command to invoke.
- color: (Optional) Color for the button. Options: blurple, gray, green, red
- emoji: (Optional) Emoji to include in the button.
- label: (Optional) Label for the button, defaults to the command name.
Usage Permissions: Staff Role or Manage Channels Permission

### /commandbutton stats
Send a button that allows players to show their stats. Usage: /commandbutton stats
Usage Permissions: Staff Role or Manage Channels Permission

## Config Loading/Saving
### /config list
List the 15 most recently created configs. Usage: /config list
Usage Permissions: Staff Role or Manage Channels Permission

### /config load
Loads the queue configuration based on the given name. Usage: /config load [config]
Arguments:
- config: (Required) Config name.
Usage Permissions: Staff Role or Manage Channels Permission

### /config save
Save the current queue configuration to a name. Usage: /config save (name)
Arguments:
- name: (Optional) Name of new config code, or omit for a random code.
Usage Permissions: Staff Role or Manage Channels Permission

## Cross Chat
Join/create a crosschat room, to share a text channel between servers. Usage: /crosschat join (room_name) (censored)
Arguments:
- room_name: (Optional) Name of the room.
- censored: (Optional) If crosschat text should be censored.
Usage Permissions: Staff Role or Manage Channels Permission

### /crosschat leave
Leave the crosschat. Usage: /crosschat leave
Usage Permissions: Staff Role or Manage Channels Permission


## Dodge
Auto ban players who cause a match to cancel by not joining the voice channel. Usage: /dodge autoban (duration)
Arguments:
- duration: (Optional) Duration of time in seconds for the ban to last, or 0 to reset.
Usage Permissions: Staff Role or Manage Channels Permission

### /dodge mmrpenalty
Deduct MMR from players who dodge the match. Usage: /dodge mmrpenalty [amount]
Arguments:
- amount: (Required) Amount of MMR to deduct.
Usage Permissions: Staff Role or Manage Channels Permission

### /dodge pointspenalty
Deduct points from players who dodge the match. Usage: /dodge pointspenalty [amount]
Arguments:
- amount: (Required) Amount of points to deduct.
Usage Permissions: Staff Role or Manage Channels Permission

## End Queue
Ends the running queue. Usage: /endqueue
Usage Permissions: Staff Role or Manage Channels Permission

## Force Start
Sets the requirements for forcestarting. Usage: /forcestartconfig conditions [min_size] (max_size) (only_fair) (auto_start)
Arguments:
- min_size: (Required) Enter the minimum number of players required. Set to -1 to disable.
- max_size: (Optional) Enter the maximum number of players required. Set to -1 to ignore.
- only_fair: (Optional) Should the forcestart happen if teams are not the same size?.
- auto_start: (Optional) Should the forcestart vote automatically happen when possible?.
Usage Permissions: Staff Role or Manage Channels Permission

### /forcestartconfig cooldown
(Default: 300) Sets the forcestart cooldown. Usage: /forcestartconfig cooldown [seconds]
Arguments:
- seconds: (Required) Cooldown duration in seconds.
- Usage Permissions: Staff Role or Manage Channels Permission

## Game Integrations
Specify whether players must register their account before playing. Usage: /requireregister [mode]
Arguments:
- mode: (Required) Game to register with, or None to disable. Options: None, Valorant, Rainbow 6, Overwatch, RocketLeague, Custom API, Manually

With register mode being Custom API, please check out https://docs.neatqueue.com/#/?id=webhooks With register mode Manually, players must have their MMR manually set, either through an admin command or via an API request https://docs.neatqueue.com/#/?id=endpoints.

Usage Permissions: Staff Role or Manage Channels Permission

## Gamemodes
Sets whether players can reshuffle gamemodes in random gamemode selection. Usage: /gamemode reshuffle [toggle] (reshuffle_limit)
Arguments:
- toggle: (Required) Whether reshuffling is enabled or disabled. Options: Enabled, Disabled
- reshuffle_limit: (Optional) How many times players can reshuffle gamemodes.
Usage Permissions: Staff Role or Manage Channels Permission

### /gamemode selection
Choose how gamemodes are selected. Usage: /gamemode selection [gamemode_choice]
Arguments:
- gamemode_choice: (Required) Voting, always random, ordered, or least common. Options: Vote, Random, Least Frequent, Ordered
Usage Permissions: Staff Role or Manage Channels Permission

## Heroes
Adds the given hero. Usage: /hero add [hero_name]
Arguments:
- hero_name: (Required) New hero name.
Usage Permissions: Staff Role or Manage Channels Permission

### /hero bans
Specify the number of hero bans or 0 to disable. Usage: /hero bans [bans] (per_team)
Arguments:
- bans: (Required) Number of bans (per team if applicable).
- per_team: (Optional) If the hero bans are team by team.
Usage Permissions: Staff Role or Manage Channels Permission

### /hero remove
Removes the given hero. Usage: /hero remove [hero_name]
Arguments:
- hero_name: (Required) The hero to remove, or ALL to remove all.
Usage Permissions: Staff Role or Manage Channels Permission

### /hero voting
Specify who can vote for hero bans. Defaults to All if no captains. Usage: /hero voting [per_team] [mode]
Arguments:
- per_team: (Required) If the map vote goes team by team. Team 1 picks first ban, Team 2 picks next, ...
- mode: (Required) Who can vote. Options: All, Captains
Usage Permissions: Staff Role or Manage Channels Permission

## Info
View information about the queue configuration. Usage: /info
Usage Permissions: Staff Role or Manage Channels Permission

## Language
Set the language for the server. Usage: /language set [language]
Arguments:
- language: (Required) Server language. Options: English, Spanish, French, Portuguese, Japanese, Russian, German, Italian, Ukrainian, Polish, Hebrew, Arabic, Bengali, Hindi, Turkish, Vietnamese, Chinese Traditional, Uwu, Owo
- If there is an issue with a normal language translation, please fix here: https://crowdin.com/project/neatqueue

Usage Permissions: Staff Role or Manage Channels Permission

## Leaderboard Config

Leaderboard titles are hyperlinks to the website version of the leaderboard.

### /leaderboardconfig edits
Specify who can edit a leaderboard. Usage: /leaderboardconfig edits [edits]
Arguments:
- edits: (Required) Who can edit the leaderboard buttons. Options: Staff, Anyone, Creator
Usage Permissions: Staff Role or Manage Channels Permission

### /leaderboardconfig ignoreroles add
Will not show players on leaderboard with this role. Usage: /leaderboardconfig ignoreroles add [role]
Arguments:
- role: (Required) Required role to show on leaderboard.
Usage Permissions: Staff Role or Manage Channels Permission

### /leaderboardconfig ignoreroles remove
Remove an ignored leaderboard role. Usage: /leaderboardconfig ignoreroles remove [role]
Arguments:
- role: (Required) Role to no longer ignore.
Usage Permissions: Staff Role or Manage Channels Permission

### /leaderboardconfig monthly
Toggle monthly leaderboards, either resets monthly or rolls over. Usage: /leaderboardconfig monthly [toggle] (mode)
Arguments:
- toggle: (Required) If monthly leaderboards are enabled. Options: Enabled, Disabled
- mode: (Optional) If stats reset for the month, or keep rolling. Options: Reset, Rolling
Usage Permissions: Staff Role or Manage Channels Permission

### /leaderboardconfig requiredgames
(Default: 1) The required number of games played to be displayed on the leaderboard. Usage: /leaderboardconfig requiredgames [games]
Arguments:
-games: (Required) Required number of games.
Usage Permissions: Staff Role or Manage Channels Permission

### /leaderboardconfig sharedstats serverwide
Toggle having player stats be shared among all queues. Usage: /leaderboardconfig sharedstats serverwide [toggle] (name)
Arguments:
- toggle: (Required) If player stats are server wide. Options: Enabled, Disabled
- name: (Optional) Shared stats name, or omit to automatically determine.
Usage Permissions: Staff Role or Manage Channels Permission

### /leaderboardconfig sharedstats set
Sets the name to use for stats storaged. Queues with the same name share stats. Usage: /leaderboardconfig sharedstats set [name]
Arguments:
- name: (Required) Shared stats configuration name.
Usage Permissions: Staff Role or Manage Channels Permission

### /leaderboardconfig type
Toggle using the image or text leaderboard. Usage: /leaderboardconfig type [type]
Arguments:
- type: (Required) Leaderboard format. Options: Images, Text
Usage Permissions: Staff Role or Manage Channels Permission


## Link Queue
Links the current channel to another channel's queue. Usage: /link [channel]
Arguments:
- channel: (Required) Enter the channel to link to.
Usage Permissions: Staff Role or Manage Channels Permission

### /unlink
Unlinks the current channel. Usage: /unlink
Usage Permissions: Staff Role or Manage Channels Permission

## Lobby Channel
### /lobbychannel automute
If the lobby channel should mute all players. Usage: /lobbychannel automute [toggle]
Arguments:
- toggle: (Required) If players are muted in the lobby channel. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /lobbychannel pause
Pause the current lobby channel countdown timer. Usage: /lobbychannel pause
Usage Permissions: Staff Role or Manage Channels Permission

### /lobbychannel pullall
Specify pulling players from all channels when their match starts. Usage: /lobbychannel pullall [toggle]
Arguments:
- toggle: (Required) Pull players from all channels. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /lobbychannel returnall
Specify returning players to their original voice channel from before the match. Usage: /lobbychannel returnall [toggle]
Arguments:
- toggle: (Required) Return players to their original voice channel. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /lobbychannel set
Specify the voice channel to move players to/from before/after a game. Usage: /lobbychannel set [channel]
Arguments:
- channel: (Required) Channel to drag/drop players from/to.
Usage Permissions: Staff Role or Manage Channels Permission

### /lobbychannel timer
Specify how long players have to join the voice channel before the match is cancelled. Usage: /lobbychannel timer [timer]
Arguments:
- timer: (Required) (Default: 300) Timeout length in seconds.
Usage Permissions: Staff Role or Manage Channels Permission

### /lobbychannel toggle
Toggle creating a voice channel when a match is created for lobby setup. Usage: /lobbychannel toggle [toggle]
Arguments:
- toggle: (Required) If a new voice channel is made for each lobby setup. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /lobbychannel unpause
Unpause the current lobby channel countdown timer. Usage: /lobbychannel unpause
Usage Permissions: Staff Role or Manage Channels Permission

## Lobby Details
Sets the lobby details message. Usage: /lobbydetails location [location]
Arguments:
- location: (Required) Where to show lobby details. Options: DMs, Teams Message
Usage Permissions: Staff Role or Manage Channels Permission

### /lobbydetails remove
Removed the lobby details message. Usage: /lobbydetails remove
Usage Permissions: Staff Role or Manage Channels Permission

### /lobbydetails set
Sets the lobby details message. Usage: /lobbydetails set [message]
Arguments:
message: (Required) Enter the message to send.
Currently supports five substitutions:

- HOST: Randomly select a player name
- QUEUENUM: Substitute the queue number
- RANDOMTEAM: Substitute a random team name
- RANDOM[Option1,Option2,...]: Randomly select one of the given options and substitute. Ex: RANDOM[Heads,Tails]
- PASSWORD#T: Generate a random string of characters, where # is the length of the password, and T is the type of characters to be in the password. There are currently 5 supported password types:

L: Lowercase Letters only
U: Uppercase Letters only
N: Numbers only
C: Lowercase and Uppercase Letters
A: Lowercase Letters, Uppercase Letters, and Numbers

Example: /lobbydetails set "Host: HOST, Lobby Name: QUEUENUM, Lobby Password: PASSWORD8A could substitute to
"Host: @NeatZ, Lobby Name: 12345, Lobby Password: D83mA76x"

You can further enhance the visuals using Markdown formatting.
Usage Permissions: Staff Role or Manage Channels Permission

## Lock
Lock the queue channel to prevent players from joining. Usage: /lock (all)
Arguments:
- all: (Optional) Lock all queues?.
Usage Permissions: Staff Role or Manage Channels Permission

### /unlock
Unlock the queue channel to allow players to join. Usage: /unlock (all)
Arguments:
- all: (Optional) Unlock all queues?.
Usage Permissions: Staff Role or Manage Channels Permission

## Logs
View a log of used NeatQueue commands. Usage: /logs (filter)
Arguments:
- filter: (Optional) Filter for logs containing this word.
Usage Permissions: Staff Role or Manage Channels Permission

## MMR Change
### /mmr change allow_disable
Sets if the vote to disable MMR appears. Usage: /mmr change allow_disable [allow_disable]
Arguments:
- allow_disable: (Required) If MMR changes should be toggleable.
Usage Permissions: Staff Role or Manage Channels Permission

### /mmr change hidden
Sets if MMR changes are hidden from players. Usage: /mmr change hidden [hidden]
Arguments:
- hidden: (Required) If MMR changes are hidden.
Usage Permissions: Staff Role or Manage Channels Permission

### /mmr change mode
(Default: Per Player) Sets if MMR changes are calculated per player, or per team. Usage: /mmr change mode [mode]
Arguments:
- mode: (Required) How MMR changes are calculated. Options: Per Player, Per Team
- MMR multipliers will still be applied on a per-player basis. Disable multipliers to make everyone on the team get the same MMR change.
Usage Permissions: Staff Role or Manage Channels Permission

### /mmr change set
(Default: 50) Sets the MMR change per game. Usage: /mmr change set [amount] (loser_mmr) (static)
Arguments:
- amount: (Required) The average MMR change for wins and losses.
- loser_mmr: (Optional) Override the MMR change for losses.
- static: (Optional) If the MMR change should ALWAYS be this value.
Usage Permissions: Staff Role or Manage Channels Permission

### /mmr change variance
Sets the variance value. Lower value = higher ranges of MMR changes. Usage: /mmr change variance [amount]
Arguments:
- amount: (Required) (Default: 1600) Variance value. See docs for a calculator.
- Calculator: https://www.desmos.com/calculator/3qtwvlrw8q 
Using the calculator, you can see that as the variance value goes up, the actually outputted MMR change has lower variance, becoming less sensitive to the difference between player's MMR. In the example with a loser at 1000 MMR and a winner at 1100 MMR, the default variance produces an adjustment of 46.4 MMR for the winner.

https://www.desmos.com/calculator/3qtwvlrw8q 
Usage Permissions: Staff Role or Manage Channels Permission

### /mmr decay
Enable/disable MMR decay and configure the values. Usage: /mmr decay [toggle] (amount) (amount_type) (duration) (minimum)
Arguments:
- toggle: (Required) Enable/disable MMR decay. Options: Enabled, Disabled
- amount: (Optional) (Default: 20) Amount of MMR to decay.
- amount_type: (Optional) (Default: Static Value) If the amount is an static value, or a percentage of total MMR. Options: Static Value, Percentage
- duration: (Optional) (Default: 1 week) After how long should a player decay in seconds.
- minimum: (Optional) (Default: None) Lowest MMR a player will decay to, omit to remove.
Usage Permissions: Staff Role or Manage Channels Permission

### /mmr maximum
Sets the highest mmr a player can reach in this queue. Usage: /mmr maximum (mmr)
Arguments:
- mmr: (Optional) Enter the peak rating, or omit to reset.
Usage Permissions: Staff Role or Manage Channels Permission

### /mmr minimum
Sets the lowest mmr a player can reach in this queue. Usage: /mmr minimum (mmr)
Arguments:
- mmr: (Optional) Enter the lowest rating, or omit to reset.
Usage Permissions: Staff Role or Manage Channels Permission

### /mmr multipliers placements
Toggle the placement matches multiplier. Usage: /mmr multipliers placements [toggle]
Arguments:
- toggle: (Required) If there exists a multiplier for the first 10 matches. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /mmr multipliers remove
Remove the MMR multiplier for the given role. Usage: /mmr multipliers remove [role]
Arguments:
- role: (Required) Role to remove multiplier for.
Usage Permissions: Staff Role or Manage Channels Permission

### /mmr multipliers set
Sets the MMR multiplier for the given role for wins. Usage: /mmr multipliers set [role] [multiplier]
Arguments:
- role: (Required)
- multiplier: (Required) Multiplier value. (Ex: 1.2 for a 20% boost).
Usage Permissions: Staff Role or Manage Channels Permission

### /mmr multipliers streaks
Toggle the streak multiplier. Usage: /mmr multipliers streaks [toggle]
Arguments:
- toggle: (Required) If there exists a multiplier for win/loss streaks. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /mmr requirement
Sets the required mmr to enter this queue. Usage: /mmr requirement (minimum_mmr) (maximum_mmr)
Arguments:
- minimum_mmr: (Optional) Enter the lowest MMR a player must be to join the queue, or omit to disable.
- maximum_mmr: (Optional) Enter the highest MMR a player can be to join the queue, or omit to disable.
Usage Permissions: Staff Role or Manage Channels Permission

## MVPs
(Default: 5) MMR reward for MVPs. Usage: /mvp reward [amount]
Arguments:
- amount: (Required) Amount of MMR to give as a reward.
Usage Permissions: Staff Role or Manage Channels Permission

### /mvp toggle
Enable/disable MVP votes for matches. Usage: /mvp toggle [toggle]
Arguments:
- toggle: (Required) Enable/disable MVPs. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /mvp voterequired
(Default: Disabled) Require players to vote for MVP before voting for winner. Usage: /mvp voterequired [toggle]
Arguments:
- toggle: (Required) If voting for MVP is required. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

## Manage Players
Adds the given player to the queue. Usage: /player add [user] (role) (team)
Arguments:
- user: (Required)
- role: (Optional) Enter the role for the player.
- team: (Optional) Enter the team for the player if desired.
Usage Permissions: Staff Role or Manage Channels Permission

### /player ban
Bans a player from queuing for the given duration of time. Usage: /player ban [player] (days) (hours) (minutes) (seconds) (reason)
Arguments:
- player: (Required) The player to ban.
- days: (Optional) Days to ban for.
- hours: (Optional) Hours to ban for.
- minutes: (Optional) Minutes to ban for.
- seconds: (Optional) Seconds to ban for.
- reason: (Optional)
Usage Permissions: Staff Role or Manage Channels Permission

### /player banlist clear
Clears the ban list. Usage: /player banlist clear
Usage Permissions: Staff Role or Manage Channels Permission

### /player banlist show
View the player ban list. Usage: /player banlist show
Usage Permissions: Staff Role or Manage Channels Permission

### /player remove
Removes the given player from the queue. Usage: /player remove [user]
Arguments:
- user: (Required) The player.
Usage Permissions: Staff Role or Manage Channels Permission

### /player sub
Substitute the first player for the second player. Usage: /player sub [player1] [player2] (gamenum)
Arguments:
- player1: (Required) Enter the player to replace.
- player2: (Required) Enter the player that will be inserted.
- gamenum: (Optional) Game to modify. Can be omitted to use this channels game.
Usage Permissions: Staff Role or Manage Channels Permission

### /player unban
Unban the given player from queuing. Usage: /player unban [player]
Arguments:
- player: (Required) The player to unban.
Usage Permissions: Staff Role or Manage Channels Permission

## Manage Stats
Copies the player stats from the old queue name to the new one. Usage: /managestats copy [old_name] [new_name]
Arguments:
- old_name: (Required) Old queue name with stats.
- new_name: (Required) New name to copy the stats to. Will overwrite any stats stored there.
Usage Permissions: Staff Role or Manage Channels Permission

### /managestats merge
Merges stats from the first queue name into the second queue name. Usage: /managestats merge [from_queue_name] [to_queue_name] (mmr_merge_strategy)
Arguments:
- from_queue_name: (Required) Queue to merge stats from.
- to_queue_name: (Required) Queue to merge stats into.
- mmr_merge_strategy: (Optional) How individual MMRs should be merged together. Options: Maximum, Add Together, Average, Ignore
Usage Permissions: Staff Role or Manage Channels Permission

### /managestats move
Moves the player stats from the old queue name to the new one. Usage: /managestats move [old_name] [new_name]
Arguments:
- old_name: (Required) Old queue name with stats.
- new_name: (Required) New name to move the stats to. Will overwrite any stats stored there.
Usage Permissions: Staff Role or Manage Channels Permission

### /managestats reset all
Resets all stats for all queues, or for the inputted queue name. Usage: /managestats reset all (queue_name)
Arguments:
- queue_name: (Optional) The queue name to reset stats for.
Usage Permissions: Staff Role or Manage Channels Permission

### /managestats reset mmr
Resets all MMR for all queues, or for the inputted queue name. Usage: /managestats reset mmr (queue_name)
Arguments:
- queue_name: (Optional) The queue name to reset stats for.
Usage Permissions: Staff Role or Manage Channels Permission

### /managestats reset player
Reset the user's data for all queues or a certain queue. Usage: /managestats reset player [user] (queue_name)
Arguments:
- user: (Required) Enter the desired user.
- queue_name: (Optional) Enter the queue data to remove from. Ignore to delete all data from all queues.
Usage Permissions: Staff Role or Manage Channels Permission

## Maps
Adds the given map. Usage: /map add [map_name] (game_modes) (image_url)
Arguments:
- map_name: (Required) New map name.
- game_modes: (Optional) Comma separated list of game modes for map, if applicable.
- image_url: (Optional) Image to show when map selected.
Usage Permissions: Staff Role or Manage Channels Permission

### /map bans
Specify the number of map bans per team, or 0 to disable. Usage: /map bans [bans] (per_team)
Arguments:
- bans: (Required) Number of bans per team.
- per_team: (Optional) If the map bans are team by team.
Usage Permissions: Staff Role or Manage Channels Permission

### /map remove
Removes the given map. Usage: /map remove [map_name]
Arguments:
- map_name: (Required) The map to remove, or ALL to remove all.
- Usage Permissions: Staff Role or Manage Channels Permission

### /map reshuffle
Sets whether players can reshuffle maps in random map selection. Usage: /map reshuffle [toggle] (reshuffle_limit)
Arguments:
- toggle: (Required) Whether reshuffling is enabled or disabled. Options: Enabled, Disabled
- reshuffle_limit: (Optional) How many times players can reshuffle maps.
Usage Permissions: Staff Role or Manage Channels Permission

### /map selection
Choose how maps are selected. Usage: /map selection [map_choice]
Arguments:
- map_choice: (Required) Voting, always random, or least common. Options: Vote, Random, Least Frequent
Usage Permissions: Staff Role or Manage Channels Permission

### /map voting
Specify who can vote for map picks and map bans. Defaults to All if no captains. Usage: /map voting [per_team] [mode]
Arguments:
- per_team: (Required) If the map vote goes team by team. Team 1 picks first map, Team 2 picks next, ...
- mode: (Required) Who can vote. Options: All, Captains
Usage Permissions: Staff Role or Manage Channels Permission

## Match Start
(Default: Enabled) Send a notification DM to all players when a match starts. Usage: /matchstart dmplayers [toggle]
Arguments:
- toggle: (Required) If players are DMed on start. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /matchstart removefromqueues
(Default: Enabled) Remove players from other queues when a match starts. Usage: /matchstart removefromqueues [toggle]
Arguments:
- toggle: (Required) If players are removed from queues on start. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /matchstart shuffleonstart
(Default: Disabled) Shuffle the player pool on start. Usage: /matchstart shuffleonstart [mode]
Arguments:
- mode: (Required) Options: Disabled, Lottery, Priority
Usage Permissions: Staff Role or Manage Channels Permission

### /matchstart when
(Default: Either) Start the match when the queue fills, or only when forcestarted. Usage: /matchstart when [mode]
Arguments:
- mode: (Required) Condition for starting the match. Options: Queue Filled, Forcestart, Either
Usage Permissions: Staff Role or Manage Channels Permission

## Matchmaking
The matchmaker works by checking the current queue if there are enough players to create a match. A match will only be created if the total range of player MMRs is less than the specified matchmaking range. Every 15 seconds, the range will be increased by the matchmaking leniency, and the match conditions will be rechecked with this new extended matchmaking range.

### /matchmaking leniency
Every 15 seconds, how much the range will increase for a better chance at a match. Usage: /matchmaking leniency [value]
Arguments:
- value: (Required) How much to increase the range by.
Usage Permissions: Staff Role or Manage Channels Permission

### /matchmaking range
The range of MMRs for matches. Tighter range = more waiting and players required. Usage: /matchmaking range [range]
Arguments:
- range: (Required) Range of player MMRs.
Usage Permissions: Staff Role or Manage Channels Permission

## Messages + Styling
### /message queuemessage delay
(Default: 3) Sets the delay for when a new queue message comes up. Usage: /message queuemessage delay [seconds]
Arguments:
- seconds: (Required) New message delay.
Usage Permissions: Staff Role or Manage Channels Permission

### /message queuemessage deletions
(Default: Enabled) Sets whether old queue updates should be deleted.
Usage: /message queuemessage deletions [toggle]
Arguments:
- toggle: (Required) Toggle between editing queue updates, or sending new messages. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /message queuemessage edits
(Default: Enabled) Set whether queue updates should edit the previous message. Usage: /message queuemessage edits [toggle]
Arguments:
- toggle: (Required) Toggle between editing queue updates, or sending new messages. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /message queuemessage history
(Default: Disable) Sets whether to send a new message for every queue interaction. Usage: /message queuemessage history [toggle]
Arguments:
- toggle: (Required) Toggle between sending queue join/leaves in the channel. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /message queuemessage leaderboardbutton
Show a 'Leaderboard' button on the queue message. Usage: /message queuemessage leaderboardbutton [toggle]
Arguments:
- toggle: (Required) If the leaderboard button is shown. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /message queuemessage sticky
(Default: Enabled) Sets whether the queue message sticks to the bottom of the channel. Usage: /message queuemessage sticky [toggle]
Arguments:
- toggle: (Required) Toggle the message being sticky. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /message winnermessage format
Sets the format for the winner message. Usage: /message winnermessage format [mode]
Arguments:
- mode: (Required) Formatting type. Options: Detailed, Simple
Usage Permissions: Staff Role or Manage Channels Permission

### /message winnermessage pin
Sets whether the message gets pinned. Usage: /message winnermessage pin [mode]
Arguments:
- mode: (Required) Pin mode. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /message winnermessage results
Set who can vote for the result, or if results are fully disabled. Usage: /message winnermessage results [value]
Arguments:
- value: (Required) Who can vote, or if the match has no outcome. Options: Default, Staff Only, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /message winnermessage sticky
Sets whether the message sticks to the bottom of chat. Usage: /message winnermessage sticky [mode]
Arguments:
- mode: (Required) Sticky mode. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

## Miscellaneous/Utility
### /misc mention teamscreated
(Default: Disabled) Mention the players after teams are created. Usage: /misc mention teamscreated [toggle]
Arguments:
- toggle: (Required) If the players are mentioned after teams are created. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /misc nametype
Sets whether to use nicknames or discord names (Default: nick). Usage: /misc nametype [type]
Arguments:
- type: (Required) The type of names to be used. Options: Discord, Nicknames
Usage Permissions: Staff Role or Manage Channels Permission

### /misc purge
Delete ALL messages in the channel except the queue message if it exists. Usage: /misc purge
Usage Permissions: Staff Role or Manage Channels Permission

## Mod Channel
### /staffchannel remove
Remove the set results channel. Usage: /staffchannel remove
Usage Permissions: Staff Role or Manage Channels Permission

### /staffchannel set
Sets the results channel to send queue history. Usage: /staffchannel set [channel] (serverwide)
Arguments:
- channel: (Required) The text channel to send queue history to.
- serverwide: (Optional) Should the channel be global for all queues or just this one?.
Usage Permissions: Staff Role or Manage Channels Permission

## Modify Player Data
### /add decaygraceperiod
Add a grace period for a user so they won't be affected by MMR decay. Usage: /add decaygraceperiod [time] (user) (role)
Arguments:
- time: (Required) Enter the desired grace period time in seconds.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /add game
Increment the players games, use a negative number to decrement. Usage: /add game (games) (user) (role)
Arguments:
- games: (Optional) Enter the desired games to add.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /add loss
Increment the players losses, use a negative number to decrement. Usage: /add loss (losses) (user) (role)
Arguments:
- losses: (Optional) Enter the desired losses to add.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /add mmr
Increment the players mmr, use a negative number to decrement. Usage: /add mmr (mmr) (user) (role)
Arguments:
- mmr: (Optional) Enter the desired mmr to add.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /add mvps
Increment the players MVPs, use a negative number to decrement. Usage: /add mvps [mvps] (user) (role)
Arguments:
- mvps: (Required) Enter the desired MVPs to add.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /add peakmmr
Increment the players peak mmr, use a negative number to decrement. Usage: /add peakmmr [mmr] (user) (role)
Arguments:
- mmr: (Required) Enter the desired mmr to add.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /add peakstreak
Increment the players peak streak, use a negative number to decrement. Usage: /add peakstreak [streak] (user) (role)
Arguments:
- streak: (Required) Enter the desired streak to add.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /add points
Increment the players points (not MMR), use a negative number to decrement. Usage: /add points [points] (user) (role)
Arguments:
- points: (Required) Enter the desired points to add.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /add streak
Increment the players streak, use a negative number to decrement. Usage: /add streak (streak) (user) (role)
Arguments:
- streak: (Optional) Enter the desired streak to add.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /add win
Increment the players wins, use a negative number to decrement. Usage: /add win (wins) (user) (role)
Arguments:
- wins: (Optional) Enter the desired wins to add.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /set games
Sets the players games. Usage: /set games [games] (user) (role)
Arguments:
- games: (Required) Enter the desired games.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /set ign
Sets the players IGN (used in /register or /ign). Usage: /set ign [account] (user) (role)
Arguments:
- account: (Required) Enter the desired IGN, or 'none' to remove.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /set losses
Sets the players losses. Usage: /set losses [losses] (user) (role)
Arguments:
- losses: (Required) Enter the desired losses.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /set mmr
Sets the players mmr. Usage: /set mmr [mmr] (user) (role)
Arguments:
- mmr: (Required) Enter the desired mmr.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /set mvps
Sets the players MVPs. Usage: /set mvps [mvps] (user) (role)
Arguments:
- mvps: (Required) The new MVPs amount.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /set peakmmr
Sets the players peak mmr. Usage: /set peakmmr [mmr] (user) (role)
Arguments:
- mmr: (Required) Enter the desired mmr.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /set peakstreak
Sets the players peak streak. Usage: /set peakstreak [streak] (user) (role)
Arguments:
- streak: (Required) Enter the desired streak.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /set points
Sets the players points (not MMR). Usage: /set points [points] (user) (role)
Arguments:
- points: (Required) The new points amount.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /set streak
Sets the players streak. Usage: /set streak [streak] (user) (role)
Arguments:
- streak: (Required) Enter the desired streak.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

### /set wins
Sets the players wins. Usage: /set wins [wins] (user) (role)
Arguments:
- wins: (Required) Enter the desired wins.
- user: (Optional) The user to modify.
- role: (Optional) The role to modify.
Usage Permissions: Staff Role or Manage Channels Permission

## Lobby Configuration

### /numberoflobbies  
(Default: 1) Sets the number of lobbies to create. Usage: /numberoflobbies [lobbies]  
Arguments:  
- lobbies: (Required) The number of lobbies.  
Usage Permissions: Staff Role or Manage Channels Permission

## Team Configuration

### /numberofteams  
(Default: 2) Sets the number of teams. Usage: /numberofteams [number]  
Arguments:  
- number: (Required) The number of teams.  
Usage Permissions: Staff Role or Manage Channels Permission

## Party Queue Configuration
### /partyqueue maxsize  
Set the max party size that can enter the queue. Usage: /partyqueue maxsize (max_size)  
Arguments:  
- max_size: (Optional) The max party size, or omit to remove.  
Usage Permissions: Staff Role or Manage Channels Permission

### /partyqueue preventoverfill  
(Default: Enabled) Prevent a party from joining queue if it over-fills the queue. Usage: /partyqueue preventoverfill [toggle]  
Arguments:  
- toggle: (Required) If parties can overfill a queue.  
    Options: Enabled, Disabled  
Usage Permissions: Staff Role or Manage Channels Permission

### /partyqueue toggle  
Enable party queue, allowing players to create parties with /party before joining. Usage: /partyqueue toggle [toggle]  
Arguments:  
- toggle: (Required) Enable or disable party queue.  
    Options: Enabled, Disabled  
Usage Permissions: Staff Role or Manage Channels Permission

## Predictions

### /points change loss  
(Default: 100) Set how many points players gain for a loss (not MMR). Usage: /points change loss [value]  
Arguments:  
- value: (Required) Points for a loss.  
Usage Permissions: Staff Role or Manage Channels Permission

### /points change win  
(Default: 100) Set how many points players gain for a win (not MMR). Usage: /points change win [value]  
Arguments:  
- value: (Required) Points for a win.  
Usage Permissions: Staff Role or Manage Channels Permission

### /points maximum  
Sets the highest number of points a player can reach. Usage: /points maximum (points)  
Arguments:  
- points: (Optional) Enter the peak points, or omit to reset.  
Usage Permissions: Staff Role or Manage Channels Permission

### /points minimum  
Sets the lowest number of points a player can reach. Usage: /points minimum (points)  
Arguments:  
- points: (Optional) Enter the lowest points value, or omit to reset.  
Usage Permissions: Staff Role or Manage Channels Permission

### /points multipliers remove  
Remove the points multiplier for the given role. Usage: /points multipliers remove [role]  
Arguments:  
- role: (Required) Role to remove multiplier for.  
Usage Permissions: Staff Role or Manage Channels Permission

### /points multipliers set  
Sets the points multiplier for the given role. Usage: /points multipliers set [role] [multiplier]  
Arguments:  
- role: (Required)  
- multiplier: (Required) Multiplier value. (Ex: 1.2 for a 20% boost).  
Usage Permissions: Staff Role or Manage Channels Permission

### /points startingvalue  
(Default: 0) Set how many points players start with (not MMR). Usage: /points startingvalue [value]  
Arguments:  
- value: (Required) Starting points value.  
Usage Permissions: Staff Role or Manage Channels Permission

### /predictions channel  
Specify the channel to show predictions. Usage: /predictions channel [channel]  
Arguments:  
- channel: (Required) The predictions channel.  
Usage Permissions: Staff Role or Manage Channels Permission

### /predictions role  
Role to ping when a prediction opens. Usage: /predictions role [role]  
Arguments:  
- role: (Required) Role to ping.  
Usage Permissions: Staff Role or Manage Channels Permission

### /predictions timer  
Specify the duration the prediction lasts before closing. Usage: /predictions timer [timer]  
Arguments:  
- timer: (Required) (Default: 180) Prediction length in seconds.  
Usage Permissions: Staff Role or Manage Channels Permission

### /predictions toggle  
Specify the channel to show predictions. Usage: /predictions toggle [toggle]  
Arguments:  
- toggle: (Required) If predictions are enabled or disabled.  
    Options: Enabled, Disabled  
Usage Permissions: Staff Role or Manage Channels Permission

## Queue Entry Methods

### /queueentry channel set  
(BETA) Add players to the queue when they join the voice channel. Usage: /queueentry channel set (channel)  
Arguments:  
- channel: (Optional) Queue entry voice channel, or omit to remove.  
Usage Permissions: Staff Role or Manage Channels Permission

### /queueentry methods  
(BETA) Specify how players can join the queue. Usage: /queueentry methods [modes]  
Arguments:  
- modes: (Required) The methods players can use to join the queue.  
    Options: Buttons, Voice Channel, Either  
Usage Permissions: Staff Role or Manage Channels Permission

### /queueentry price  
Set how many points a player must pay to join the queue. Usage: /queueentry price [value] (payout_fee)  
Arguments:  
- value: (Required) Price in points.  
- payout_fee: (Optional) Fee to take when paying out rewards. A value of 10 means a 10% fee is applied.  
Usage Permissions: Staff Role or Manage Channels Permission

### /queueentry survey add  
Adds a new survey which players must respond to before queuing. Usage: /queueentry survey add [title] [allow_other] [options] (key) (show_in_teams_message)  
Arguments:  
- title: (Required) Title of the survey.  
- allow_other: (Required) If players can pick "Other" and manually type their response.  
- options: (Required) Comma separated list of options.  
- key: (Optional) Key which is used to store the results for a player, or omit to use the title.  
- show_in_teams_message: (Optional)  
Usage Permissions: Staff Role or Manage Channels Permission

### /queueentry survey delete  
Delete a previously added survey. Usage: /queueentry survey delete [title]  
Arguments:  
- title: (Required) Title of the survey.  
Usage Permissions: Staff Role or Manage Channels Permission

## Queue Name

### /queuename  
Sets the name for this queue. All stats are tied to the queue name. Usage: /queuename [name]  
Arguments:  
- name: (Required) New queue name.  
Usage Permissions: Staff Role or Manage Channels Permission

## Queue Type

### /queuetype  
Select the type of queue to run. See docs for detailed explanations. Usage: /queuetype [type]  
Arguments:  
- type: (Required) The type of queue.  
    Options: PUGs/Normal Individual Queue, Matchmaking, Full Team vs Full Team, Select Team On Join  
    PUGs/Normal Individual Queue: The default queue setup, players join individually to get put into a match when the queue is filled.  
    Matchmaking: Players join the queue, and once there are enough players within their MMR range, a match is created.  
    Full Team vs Full Team: Captains join the queue and pull in the entire team. No team setup is required.  
    Select Team On Join: The queue has join buttons for each team, no team setup is required.  
Usage Permissions: Staff Role or Manage Channels Permission

## Ranks/Automatically Assign Discord Roles

### /autoroles copy  
Copies the auto roles config to the desired channel. Usage: /autoroles copy [channel]  
Arguments:  
- channel: (Required) Channel with queue to copy autoroles config to.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles games remove  
Removes a condition where player roles are changed based on games. Usage: /autoroles games remove [role]  
Arguments:  
- role: (Required) Enter the role.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles games set  
(Ranks) Adds a condition in which player roles are changed based on games. Usage: /autoroles games set [role] [lower_value] [upper_value] (only_one_allowed)  
Arguments:  
- role: (Required) Role.  
- lower_value: (Required) The lowest number of games required to gain the role.  
- upper_value: (Required) The upper number of games to lose the role.  
- only_one_allowed: (Optional) (Default: True) If this role is assigned, no other games autoroles will be allowed.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles ingame  
Assign a role to players who are in a match that is removed after. Usage: /autoroles ingame (role)  
Arguments:  
- role: (Optional) Enter the role, or omit to remove.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles inqueue  
Assign a role to players who are in the queue. Usage: /autoroles inqueue (role)  
Arguments:  
- role: (Optional) Enter the role, or omit to remove.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles leaderboardposition remove  
Removes a leaderboard position role. Usage: /autoroles leaderboardposition remove [role] [stat]  
Arguments:  
- role: (Required) Enter the role.  
- stat: (Required) Stat which autoroles leaderboard position applies to.  
    Options: MMR, Peak MMR, Points, MVPs, Games, Wins, Losses, Winrate, Streak, Peak Streak  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles leaderboardposition set  
Adds a condition to give players a role based on leaderboard position. Usage: /autoroles leaderboardposition set [role] [stat] [lower_value] (upper_value)  
Arguments:  
- role: (Required) Enter the role.  
- stat: (Required) Type of leaderboard stat to use.  
    Options: MMR, Peak MMR, Points, MVPs, Games, Wins, Losses, Winrate, Streak, Peak Streak  
- lower_value: (Required) (Inclusive) Leaderboard position range 1.  
- upper_value: (Optional) (Inclusive) Leaderboard position range 2, or omit for no range.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles losses remove  
Removes a condition where player roles are changed based on losses. Usage: /autoroles losses remove [role]  
Arguments:  
- role: (Required) Enter the role.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles losses set  
(Ranks) Adds a condition in which player roles are changed based on losses. Usage: /autoroles losses set [role] [lower_value] [upper_value] (only_one_allowed)  
Arguments:  
- role: (Required) Role.  
- lower_value: (Required) The lowest number of losses required to gain the role.  
- upper_value: (Required) The upper number of losses to lose the role.  
- only_one_allowed: (Optional) (Default: True) If this role is assigned, no other loss autoroles will be allowed.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles mmr remove  
Removes a condition where player roles are changed based on MMR. Usage: /autoroles mmr remove [role]  
Arguments:  
- role: (Required) Enter the role.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles mmr set  
(Ranks) Adds a condition in which player roles are changed based on MMR. Usage: /autoroles mmr set [role] [lower_rating] [upper_rating] (lower_lose_rating) (only_one_allowed)  
Arguments:  
- role: (Required) Role.  
- lower_rating: (Required) The lowest MMR required to gain the role.  
- upper_rating: (Required) The upper MMR rating to lose the role.  
- lower_lose_rating: (Optional) (Default: lower_rating) The MMR the player must fall below to lose the role.  
- only_one_allowed: (Optional) (Default: True) If this role is assigned, no other MMR autoroles will be allowed.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles mvps remove  
Removes a condition where player roles are changed based on mvps. Usage: /autoroles mvps remove [role]  
Arguments:  
- role: (Required) Enter the role.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles mvps set  
(Ranks) Adds a condition in which player roles are changed based on mvps. Usage: /autoroles mvps set [role] [lower_value] [upper_value] (only_one_allowed)  
Arguments:  
- role: (Required) Role.  
- lower_value: (Required) The lowest number of mvps required to gain the role.  
- upper_value: (Required) The upper number of mvps to lose the role.  
- only_one_allowed: (Optional) (Default: True) If this role is assigned, no other mvps autoroles will be allowed.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles notify  
Toggle sending a DM to players when their rank autorole changes. Usage: /autoroles notify [toggle]  
Arguments:  
- toggle: (Required) If players get a DM for role/rank changes.  
    Options: Enabled, Disabled  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles points remove  
Removes a condition where player roles are changed based on Points. Usage: /autoroles points remove [role]  
Arguments:  
- role: (Required) Enter the role.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles points set  
(Ranks) Adds a condition in which player roles are changed based on points. Usage: /autoroles points set [role] [lower_value] [upper_value] (only_one_allowed)  
Arguments:  
- role: (Required) Role.  
- lower_value: (Required) The lowest number of points required to gain the role.  
- upper_value: (Required) The upper number of points to lose the role.  
- only_one_allowed: (Optional) (Default: True) If this role is assigned, no other Point autoroles will be allowed.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles refresh  
Recalculates all autoroles for players. Usage: /autoroles refresh  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles reset  
Delete all auto role settings. Usage: /autoroles reset  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles streaks remove  
Removes a condition where player roles are changed based on streaks. Usage: /autoroles streaks remove [role]  
Arguments:  
- role: (Required) Enter the role.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles streaks set  
(Ranks) Adds a condition in which player roles are changed based on streaks. Usage: /autoroles streaks set [role] [lower_value] [upper_value] (only_one_allowed)  
Arguments:  
- role: (Required) Role.  
- lower_value: (Required) The lowest number of streaks required to gain the role.  
- upper_value: (Required) The upper number of streaks to lose the role.  
- only_one_allowed: (Optional) (Default: True) If this role is assigned, no other streaks autoroles will be allowed.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles winrate remove  
Removes a condition where player roles are changed based on winrate. Usage: /autoroles winrate remove [role]  
Arguments:  
- role: (Required) Enter the role.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles winrate set  
(Ranks) Adds a condition in which player roles are changed based on winrate. Usage: /autoroles winrate set [role] [lower_value] [upper_value] (only_one_allowed)  
Arguments:  
- role: (Required) Role.  
- lower_value: (Required) The lowest winrate value (0 to 100) required to gain the role.  
- upper_value: (Required) The upper winrate value (0 to 100) to lose the role.  
- only_one_allowed: (Optional) (Default: True) If this role is assigned, no other winrate autoroles will be allowed.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles wins remove  
Removes a condition where player roles are changed based on wins. Usage: /autoroles wins remove [role]  
Arguments:  
- role: (Required) Enter the role.  
Usage Permissions: Staff Role or Manage Channels Permission

### /autoroles wins set  
(Ranks) Adds a condition in which player roles are changed based on wins. Usage: /autoroles wins set [role] [lower_value] [upper_value] (only_one_allowed)  
Arguments:  
- role: (Required) Role.  
- lower_value: (Required) The lowest number of wins required to gain the role.  
- upper_value: (Required) The upper number of wins to lose the role.  
- only_one_allowed: (Optional) (Default: True) If this role is assigned, no other wins autoroles will be allowed.  
Usage Permissions: Staff Role or Manage Channels Permission

## Reaction Roles

### /reactionroles add
Specify roles to assign when users react to the message. Usage: /reactionroles add [channel] [message_id] [role] [reaction] (remove_others) (queue_role)
Arguments:
- channel: (Required) Channel where message is.
- message_id: (Required) Message to add reaction to.
- role: (Required) Role to assign/remove.
- reaction: (Required) Reaction that corresponds to this role.
- remove_others: (Optional) If the user has this role, remove all other reactionroles in the message they have.
- queue_role: (Optional) Option role for /roles that the user will default to.
Usage Permissions: Staff Role or Manage Channels Permission

## Ready Up

### /readyup mode
How players indicate they are ready to play a match. Usage: /readyup mode [mode]
Arguments:
- mode: (Required) How players show they are ready. Options: Ready Up Button, Join Lobby Voice Channel, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /readyup replaceinactive mode
Changes how a replacement is found. Usage: /readyup replaceinactive mode [mode]
Arguments:
- mode: (Required) Replacement mode. Options: Closest Rated, Highest Rated, Queue Priority
Usage Permissions: Staff Role or Manage Channels Permission

### /readyup replaceinactive toggle
Toggle replacing inactive players if possible. Usage: /readyup replaceinactive toggle [toggle]
Arguments:
- toggle: (Required) If automatic replacement is enabled. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

## Rematch

### /rematches
(Default: true) Toggle the ability to rematch. Usage: /rematches [toggle]
Arguments:
- toggle: (Required) If you want rematches to be enabled or disabled.
Usage Permissions: Staff Role or Manage Channels Permission

## Requeue
For queue types that always start when reaching the queue size, requeue priority won't appear to make any changes. However, there are two specific queue starting modes where it will matter: 
1. /queuetype Matchmaking: When the matchmaker is running, it will use the overall sum of all player priorities, and use this value to increase the matchmaking range. For example, if the matchmaking range is 300 MMR, but there are two players with 100 priority each, the matchmaking range for that attempted match creation will be 500 MMR, making it more likely for that match to be created. If you want players with priority to ALWAYS be in the match, you can give them a very large priority (like 100,000), which ensures the matchmaker always considers their match as valid. 
2. /misc startwhen Forcestarted: When matches can only be forcestarted, the number of players can exceed the maximum queue size. Players who join the queue with priority will take precedence in the queue over lower priority players.

### /requeue condition
Sets the condition for letting a player requeue. Usage: /requeue condition [condition]
Arguments:
- condition: (Required) Condition that must be met to requeue. Options: Must Vote, Winner Selected, None
Usage Permissions: Staff Role or Manage Channels Permission

### /requeue delay
Delay people from queuing for the given duration after the condition is met. Usage: /requeue delay [seconds]
Arguments:
- seconds: (Required) Seconds to delay from queuing.
Usage Permissions: Staff Role or Manage Channels Permission

### /requeue matchcancelled
Specify if players get automatically requeued if a match is cancelled. Usage: /requeue matchcancelled [mode]
Arguments:
- mode: (Required) If requeue is automatic. Options: Disabled, Automatic
Usage Permissions: Staff Role or Manage Channels Permission

### /requeue priority
Give priority to players who requeue after a match. Usage: /requeue priority (value) (seconds)
Arguments:
- value: (Optional) (Default: 0) How much priority value to give.
- seconds: (Optional) (Default: 300) How many seconds to give this temporary priority value for.
Usage Permissions: Staff Role or Manage Channels Permission

### /requeue priorityrole add
Allow players with the given role to gain priority for requeue. Usage: /requeue priorityrole add [role] (value)
Arguments:
- role: (Required) Priority role.
- value: (Optional) (Default: 100) Priority value to assign.
Usage Permissions: Staff Role or Manage Channels Permission

### /requeue priorityrole remove
Allow players with the given role to gain priority for requeue. Usage: /requeue priorityrole remove [role]
Arguments:
- role: (Required) Priority role.
Usage Permissions: Staff Role or Manage Channels Permission

## Require IGN

### /requireign
(Default: false) Require if players must set their IGN before they can queue. Usage: /requireign [toggle]
Arguments:
- toggle: (Required) If you want to require that users set their IGN. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

## Required Votes

### /requiredvotes cancel
Sets the number of votes required for cancelling a game. Usage: /requiredvotes cancel [type]
Arguments:
- type: (Required) The type of voting requirement to be used. Options: Half, Majority, One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten
Usage Permissions: Staff Role or Manage Channels Permission

### /requiredvotes default
Sets the default number of votes required. Usage: /requiredvotes default [type]
Arguments:
- type: (Required) The type of voting requirement to be used. Options: Half, Majority, One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten
Usage Permissions: Staff Role or Manage Channels Permission

### /requiredvotes forcestart
Sets the number of votes required for forcestarting a game. Usage: /requiredvotes forcestart [type]
Arguments:
- type: (Required) The type of voting requirement to be used. Options: Half, Majority, One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten
Usage Permissions: Staff Role or Manage Channels Permission

### /requiredvotes mvp
Sets the number of votes required for getting MVP. Usage: /requiredvotes mvp [type]
Arguments:
- type: (Required) The type of voting requirement to be used. Options: Half, Majority, One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten
Usage Permissions: Staff Role or Manage Channels Permission

### /requiredvotes winner
Sets the number of votes required for picking a winner. Usage: /requiredvotes winner [type]
Arguments:
- type: (Required) The type of voting requirement to be used. Options: Half, Majority, One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten
Usage Permissions: Staff Role or Manage Channels Permission

## Requirements

### /bannedroles add
Add a banned role which can't join the queue. Usage: /bannedroles add [role]
Arguments:
- role: (Required) Enter the banned role.
Usage Permissions: Staff Role or Manage Channels Permission

### /bannedroles remove
Removed a banned role. Usage: /bannedroles remove [role]
Arguments:
- role: (Required) Enter the banned role.
Usage Permissions: Staff Role or Manage Channels Permission

### /rolerequirement add
Add a required role to enter this queue. Players can join if they have any of the roles. Usage: /rolerequirement add [role]
Arguments:
- role: (Required) Enter the required role.
Usage Permissions: Staff Role or Manage Channels Permission

### /rolerequirement remove
Removed a required role to enter this queue. Usage: /rolerequirement remove [role]
Arguments:
- role: (Required) Enter the required role.
Usage Permissions: Staff Role or Manage Channels Permission

## Results Channel

### /resultschannel
Sets the channel to post match results. Usage: /resultschannel [channel]
Arguments:
- channel: (Required) Enter the desired channel.
Usage Permissions: Staff Role or Manage Channels Permission

## Roles

### /roles
(Default: None) Sets the roles for this queue, or omit to remove all. Usage: /roles (roles) (required)
Arguments:
- roles: (Optional) Enter the roles in the form Role,Role,Role,etc.
- required: (Optional) If roles are required to be chosen and enforced.
Usage Permissions: Staff Role or Manage Channels Permission

## Schedule

### /schedule cancelsetup
(BETA) Cancels your currently active schedule setup. Usage: /schedule cancelsetup
Usage Permissions: Staff Role or Manage Channels Permission

### /schedule delete
(BETA) Delete a previously scheduled command. Usage: /schedule delete [scheduled_command]
Arguments:
- scheduled_command: (Required) The scheduled command to remove.
Usage Permissions: Staff Role or Manage Channels Permission

### /schedule repeat
(BETA) Toggle if the scheduled command should repeat each time daily. Usage: /schedule repeat [scheduled_command] (repeat)
Arguments:
- scheduled_command: (Required)
- repeat: (Optional) If times should repeat after execution. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /schedule setup
(BETA) Start scheduling the execution of any NeatQueue command. Usage: /schedule setup
Usage Permissions: Staff Role or Manage Channels Permission

### /schedule time add
(BETA) Specify an execution time for the scheduled command. Usage: /schedule time add [scheduled_command] [time] (timezone)
Arguments:
- scheduled_command: (Required) The scheduled command to add an execution time for.
- time: (Required) Time for the command to be executed.
- timezone: (Optional) (Default: /timezone) Respective timezone for the inputted time.
Usage Permissions: Staff Role or Manage Channels Permission

### /schedule time list
(BETA) List the scheduled times for the command. Usage: /schedule time list [scheduled_command]
Arguments:
- scheduled_command: (Required) The scheduled command to list execution times.
Usage Permissions: Staff Role or Manage Channels Permission

### /schedule time remove
(BETA) Remove an execution time for the scheduled command. Usage: /schedule time remove [scheduled_command] [time]
Arguments:
- scheduled_command: (Required) The scheduled command to remove an execution time for.
- time: (Required) Time for the command to be executed.
Usage Permissions: Staff Role or Manage Channels Permission

## Select Winner

### /outcome cancel
Cancel the given game. Usage: /outcome cancel [match_number]
Arguments:
- match_number: (Required) The match number.
Usage Permissions: Staff Role or Manage Channels Permission

### /outcome selectwinner
Sets the winner for the given game. Usage: /outcome selectwinner [match_number] [team_num]
Arguments:
- match_number: (Required) The match number.
- team_num: (Required) The team that won.
Usage Permissions: Staff Role or Manage Channels Permission

### /outcome tie
Mark the given game as a tie. Usage: /outcome tie [match_number]
Arguments:
- match_number: (Required) The match number.
Usage Permissions: Staff Role or Manage Channels Permission

## Server Stats

### /serverstats channelnames games
Show how many games have been played by renaming the specified channel. Usage: /serverstats channelnames games (channel) (format)
Arguments:
- channel: (Optional) Channel to rename, or omit to remove.
- format: (Optional) Format for channel name. Indicate a $ for the replacement. Ex: "Games: $".
Usage Permissions: Staff Role or Manage Channels Permission

### /serverstats channelnames ingame
Show how many players are in game by renaming the specified channel. Usage: /serverstats channelnames ingame (channel) (format)
Arguments:
- channel: (Optional) Channel to rename, or omit to remove.
- format: (Optional) Format for channel name. Indicate a $ for the replacement. Ex: "In Game: $".
Usage Permissions: Staff Role or Manage Channels Permission

### /serverstats channelnames inqueue
Show how many players are in queue by renaming the specified channel. Usage: /serverstats channelnames inqueue (channel) (format)
Arguments:
- channel: (Optional) Channel to rename, or omit to remove.
- format: (Optional) Format for channel name. Indicate a $ for the replacement. Ex: "In Queue: $".
Usage Permissions: Staff Role or Manage Channels Permission

### /serverstats channelnames players
Show the total number of players by renaming the specified channel. Usage: /serverstats channelnames players (channel) (format)
Arguments:
- channel: (Optional) Channel to rename, or omit to remove.
- format: (Optional) Format for channel name. Indicate a $ for the replacement. Ex: "Players: $".
Usage Permissions: Staff Role or Manage Channels Permission

### /serverstats channelnames users
Show how many users are in the server by renaming the specified channel. Usage: /serverstats channelnames users (channel) (format)
Arguments:
- channel: (Optional) Channel to rename, or omit to remove.
- format: (Optional) Format for channel name. Indicate a $ for the replacement. Ex: "Users: $".
Usage Permissions: Staff Role or Manage Channels Permission

### /serverstats info
View all queue names in the server. Usage: /serverstats info (hidden)
Arguments:
- hidden: (Optional) If you want the stats to be hidden.
Usage Permissions: Staff Role or Manage Channels Permission

## Setup

### /setup
Starts the interactive setup. Usage: /setup
Usage Permissions: Staff Role or Manage Channels Permission

## Show MMR in Name

### /ratinginname format
(Default: '- ($)') Sets the format for ratings in nicknames. Usage: /ratinginname format [format] [location]
Arguments:
- format: (Required) How the rating should be formatted. A ' indicates the player's rating.
- location: (Required) Options: Prefix, Suffix
Usage Permissions: Staff Role or Manage Channels Permission

### /ratinginname queuenames
Sets the queue names to use in retrieving player stats, or omit to reset. Usage: /ratinginname queuenames (names)
Arguments:
- names: (Optional) The queue names separated by ',' to use for inserting ratings into ' indicators in the format.
Usage Permissions: Staff Role or Manage Channels Permission

### /ratinginname removeallnicknames
Removes all nicknames from all members. Usage: /ratinginname removeallnicknames
Usage Permissions: Staff Role or Manage Channels Permission

### /ratinginname toggle
Enable or disable showing player MMR in their nickname. Usage: /ratinginname toggle [toggle]
Arguments:
- toggle: (Required) If ratings should be shown in name. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

## Simulate

### /simulate
Simulate the MMR distribution for the current configuration. Usage: /simulate (players) (matches)
Arguments:
- players: (Optional) The number of players to simulate.
- matches: (Optional) The number of matches to simulate.
Usage Permissions: Staff Role or Manage Channels Permission

## Spectator Role

### /spectatorrole add
Specify a spectator role which can join any voice channel. Usage: /spectatorrole add [role] (can_speak)
Arguments:
- role: (Required) Spectator role.
- can_speak: (Optional) Can this role speak in the channel?.
Usage Permissions: Staff Role or Manage Channels Permission

### /spectatorrole remove
Remove's a spectator role. Usage: /spectatorrole remove [role]
Arguments:
- role: (Required) Spectator role.
Usage Permissions: Staff Role or Manage Channels Permission

## Staff

### /staffrole add
Add a staff role that grants access to commands. Usage: /staffrole add [role] [template]
Arguments:
- role: (Required) Staff role.
- template: (Required) If the role gets access to all commands or not. Options: User Commands Only, All Commands
Usage Permissions: Staff Role or Manage Channels Permission

### /staffrole command allow
Grants the staff role access to the given command. Usage: /staffrole command allow [role] [command]
Arguments:
- role: (Required) Staff role.
- command: (Required) The command to grant access to.
Usage Permissions: Staff Role or Manage Channels Permission

### /staffrole command deny
Removes the staff role's access to the given command. Usage: /staffrole command deny [role] [command]
Arguments:
- role: (Required) Staff role.
- command: (Required) The command to remove access from.
Usage Permissions: Staff Role or Manage Channels Permission

### /staffrole list
List all configured staff roles. Usage: /staffrole list
Usage Permissions: Staff Role or Manage Channels Permission

### /staffrole remove
Remove a staff role. Usage: /staffrole remove [role]
Arguments:
- role: (Required) Staff role.
Usage Permissions: Staff Role or Manage Channels Permission

### /staffrole reset
Resets the staff role to starting permissions. Usage: /staffrole reset [role]
Arguments:
- role: (Required) Staff role.
Usage Permissions: Staff Role or Manage Channels Permission

## Start From Voice Channel

### /startfromvc
Creates a queue using all players in the given channel. Usage: /startfromvc [voice_channel]
Arguments:
- voice_channel: (Required) The voice channel to start a queue from.
Usage Permissions: Staff Role or Manage Channels Permission

## Start Queue

### /startqueue
Starts a queue for the current channel. Usage: /startqueue [queuename] [teamsize] (numberofteams)
Arguments:
- queuename: (Required) Name for the queue.
- teamsize: (Required) Team size.
- numberofteams: (Optional) Number of teams in a match.
Usage Permissions: Staff Role or Manage Channels Permission

## Starting MMR

### /startingmmr remove
Removes the starting mmr for the given role. Usage: /startingmmr remove [role]
Arguments:
- role: (Required) The role to remove starting MMR from.
Usage Permissions: Staff Role or Manage Channels Permission

### /startingmmr set
Sets the starting mmr for the given role. Usage: /startingmmr set [mmr] (role)
Arguments:
- mmr: (Required) The starting mmr value.
- role: (Optional) The role.
Usage Permissions: Staff Role or Manage Channels Permission

## Stats Config

### /statsconfig graph games
Sets the maximum number of games to show in /stats. Usage: /statsconfig graph games (limit)
Arguments:
- limit: (Optional) (Default: 30) Max number of games to show.
Usage Permissions: Staff Role or Manage Channels Permission

### /statsconfig graph xaxis
Sets the x-axis labels type in /stats. Usage: /statsconfig graph xaxis [data]
Arguments:
- data: (Required) (Default: Dates) Which data to show on the x-axis in the stats graph. Options: Dates, Games
Usage Permissions: Staff Role or Manage Channels Permission

### /statsconfig hidestats
Sets whether stats are forced to be hidden (only shown to the user). Usage: /statsconfig hidestats [toggle]
Arguments:
- toggle: (Required) If you want the stats to be always hidden.
Usage Permissions: Staff Role or Manage Channels Permission

### /statsconfig rankupautorole
Sets what autorole criteria is used for displaying rank ups in /stats. Usage: /statsconfig rankupautorole [autorole]
Arguments:
- autorole: (Required) (Default: MMR) Which autorole to use. Options: MMR, Points, Wins, Losses, Games, Streak, Winrate, MVPs
Usage Permissions: Staff Role or Manage Channels Permission

## Team Creation

### /teamselection reshuffle
Sets whether players can reshuffle teams in random team selection. Usage: /teamselection reshuffle [toggle]
Arguments:
- toggle: (Required) Whether reshuffling is enabled or disabled. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /teamselection set
Choose how teams will be picked. Usage: /teamselection set
Usage Permissions: Staff Role or Manage Channels Permission

## Team Names

### /teamnames captains
If team names should be the captains names, if applicable. Usage: /teamnames captains [toggle]
Arguments:
- toggle: (Required) Toggle team names being the captain's names. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /teamnames set
Specify the names of each team, or omit for the default behavior.. Usage: /teamnames set (team_names)
Arguments:
- team_names: (Optional) Comma separated list of team names. Ex: Team 1,Team 2,...
Usage Permissions: Staff Role or Manage Channels Permission

## Team Size

### /teamsize
Sets the size for each team. Usage: /teamsize [size]
Arguments:
- size: (Required) The team size.
Usage Permissions: Staff Role or Manage Channels Permission

## Temporary Setup Channels

### /tempchannels name
(Default: queue-$) Naming format for temporary setup channels. Usage: /tempchannels name [name_format]
Arguments:
- name_format: (Required) Channel format, where $ will be replaced with the match number.
Usage Permissions: Staff Role or Manage Channels Permission

### /tempchannels permissions set
Specify a permission to set for a role when creating the temporary channel. Usage: /tempchannels permissions set [role] [permission] [value]
Arguments:
- role: (Required) Role to modify permissions for.
- permission: (Required) Permission name.
- value: (Required) Permission value. Options: Deny, Allow, Default
Usage Permissions: Staff Role or Manage Channels Permission

### /tempchannels toggle
(Default: Enabled) Sets whether to create a temporary text channel for setup. Usage: /tempchannels toggle [mode]
Arguments:
- mode: (Required) If the temporary setup channels are enabled. Options: Enabled, Disabled
Usage Permissions: Staff Role or Manage Channels Permission

### /tempchannels type
(Default: Text Channels) Specify if the temp channels are threads or normal channels. Usage: /tempchannels type [type]
Arguments:
- type: (Required) If the new channels should be text channels, or threads of this channel. Options: Text Channels, Threads
Usage Permissions: Staff Role or Manage Channels Permission

## Test

### /test
Enables testing mode which allows for duplicate queue joining. Usage: /test
Usage Permissions: Staff Role or Manage Channels Permission

## Ties

### /ties
Sets whether tieing is an option for game outcomes. Usage: /ties [toggle]
Arguments:
- toggle: (Required) Whether to show the tie option.
Usage Permissions: Staff Role or Manage Channels Permission

## Timers

### /timer afk
Toggle kicking players for inactivity. Usage: /timer afk [toggle] (timer)
Arguments:
- toggle: (Required) Toggle.
- timer: (Optional) Enter the AFK timer in seconds (Default: 3600).
Usage Permissions: Staff Role or Manage Channels Permission

### /timer matchcleanup
(Default: 5400) Sets the timeout before a running game is finished. Usage: /timer matchcleanup [seconds]
Arguments:
- seconds: (Required) Enter the time in SECONDS.
Usage Permissions: Staff Role or Manage Channels Permission

### /timer queuemessage
(Default: 3) Sets the delay for when a new queue message comes up. Usage: /timer queuemessage [seconds]
Arguments:
- seconds: (Required) New message delay.
Usage Permissions: Staff Role or Manage Channels Permission

### /timer queuereset
(Default: 3600) Sets the time before the queue is reset. Usage: /timer queuereset [seconds]
Arguments:
- seconds: (Required) Enter the time in SECONDS.
Usage Permissions: Staff Role or Manage Channels Permission

### /timer votes
(Default: 60) Sets the timeout for voting menus. Usage: /timer votes [seconds]
Arguments:
- seconds: (Required)
Usage Permissions: Staff Role or Manage Channels Permission

### /timer winnervotemessage
(Default: 0) Sets the delay before enabling the winner voting message. Usage: /timer winnervotemessage [seconds]
Arguments:
- seconds: (Required) Enter the time in SECONDS.
Usage Permissions: Staff Role or Manage Channels Permission

## Timezone

### /timezone
(Default: 'US/Eastern') Sets the server's timezone. Usage: /timezone [timezone]
Arguments:
- timezone: (Required) Server's timezone.
Usage Permissions: Staff Role or Manage Channels Permission

## Tournaments
Keep in mind that Tournaments are still in beta and bugs can ocurr.

## Tournaments

### /tournament account  
Link your server to challonge using your username and api key. Usage: /tournament account [challonge_username] [challonge_api_key]  
- challonge_username: (Required) Challonge username  
- challonge_api_key: (Required) Challonge API Key from https://challonge.com/settings/developer  
Usage Permissions: Staff Role or Manage Channels Permission  

### /tournament config autocreatematches  
(BETA) Toggle automatically creating new matches when ready. Usage: /tournament config autocreatematches [mode] (tournament_url)  
- mode: (Required) Toggle automatically creating matches. Options: Enabled, Disabled  
- tournament_url: (Optional) Tournament to edit  
Usage Permissions: Staff Role or Manage Channels Permission  

### /tournament config autocreatenewtournament  
(BETA) Toggle automatically creating new tournaments. Usage: /tournament config autocreatenewtournament [mode] (tournament_url)  
- mode: (Required) Change if new tournaments are automatically created. Options: On Start, On Completion, Never  
- tournament_url: (Optional) Tournament to edit  
Usage Permissions: Staff Role or Manage Channels Permission  

### /tournament config autostartonfill  
(BETA) Toggle automatically starting the tournament when filled. Usage: /tournament config autostartonfill [mode] (tournament_url)  
- mode: (Required) Toggle automatically starting on fill. Options: Enabled, Disabled  
- tournament_url: (Optional) Tournament to edit  
Usage Permissions: Staff Role or Manage Channels Permission  

### /tournament config details  
(BETA) Change the tournament details shown in the queue message. Usage: /tournament config details (details) (tournament_url)  
- details: (Optional) Tournament details, or omit to remove  
- tournament_url: (Optional) Tournament to edit  
Usage Permissions: Staff Role or Manage Channels Permission  

### /tournament create  
(BETA) Create a new tournament and shows signup buttons. Usage: /tournament create [maximum_participants] (tournament_type) (auto_start_on_fill) (auto_create_matches) (auto_create_new_tournament) (team_size) (name) (url) (details) (forfeit_timer_sec)  
- maximum_participants: (Required) Maximum number of teams that can register  
- tournament_type: (Optional) (Default: Single Elimination) Tournament type. Options: single_elimination, double_elimination, round_robin, swiss  
- auto_start_on_fill: (Optional) (Default: True) Automatically start the tournament when the participant capacity is hit  
- auto_create_matches: (Optional) (Default: True) If the bot should automatically create matches when ready  
- auto_create_new_tournament: (Optional) (Default: On Completion) Automatically create a new tournament when this one starts/ends?. Options: On Start, On Completion, Never  
- team_size: (Optional) Number of players on each team  
- name: (Optional) The tournament name  
- url: (Optional) Challonge tournament URL, or omit to auto generate  
- details: (Optional) Any extra details to show in the queue message  
- forfeit_timer_sec: (Optional) How longer players have to join the match (in seconds) before forfeiting  
Usage Permissions: Staff Role or Manage Channels Permission  

### /tournament delete  
(BETA) Deletes the tournament. Usage: /tournament delete (tournament_url)  
- tournament_url: (Optional) Tournament to delete  
Usage Permissions: Staff Role or Manage Channels Permission  

### /tournament refresh  
(BETA) Refresh necessary data from challonge and start any required matches. Usage: /tournament refresh (tournament_url)  
- tournament_url: (Optional) Tournament to refresh  
Usage Permissions: Staff Role or Manage Channels Permission  

### /tournament start  
(BETA) Start the tournament. Usage: /tournament start (tournament_url)  
- tournament_url: (Optional) Tournament to start  
Usage Permissions: Staff Role or Manage Channels Permission  

### /tournament startmatches  
(BETA) Starts the next set of ready matches. Usage: /tournament startmatches (tournament_url)  
- tournament_url: (Optional) Tournament to start matches for  
Usage Permissions: Staff Role or Manage Channels Permission  

## Voice Channel Mode

### /voicechannels moveteam  
(Default: After All Setup) Sets when to move players to team voice channels. Usage: /voicechannels moveteam [when]  
- when: (Required) When to move players to team channels. Options: After All Setup, After Teams Created  
Usage Permissions: Staff Role or Manage Channels Permission  

### /voicechannels permissions set  
Specify a permission to set for a role when creating voice channels. Usage: /voicechannels permissions set [role] [permission] [value]  
- role: (Required) Role to modify permissions for  
- permission: (Required) Permission name  
- value: (Required) Permission value. Options: Deny, Allow, Default  
Usage Permissions: Staff Role or Manage Channels Permission  

### /voicechannels teamchannels  
(Default: Enabled) Toggle creating separate voice channels for each team. Usage: /voicechannels teamchannels [toggle]  
- toggle: (Required) If channels are created per team. Options: Enabled, Disabled  
Usage Permissions: Staff Role or Manage Channels Permission  

## Voting Menu

### /votingmenu add  
Add a new voting menu. Usage: /votingmenu add [title] [options] [key] [team_voting] (order) (button_colors) (show_numbers) (allow_random) (force_random) (number_of_votes)  
- title: (Required) (Ex: Vote for the Region) The title for the vote  
- options: (Required) (Ex: NA,EU) Comma separated list of options. Ignored if options_variable exists with values  
- key: (Required) (Ex: Region Name) The key for this vote for displaying the result after  
- team_voting: (Required) Is the vote once per team, once for all teams, or for a specific team?  
- order: (Optional) (Ex: 1) The order for this vote in regard to other votes. Votes will occur in ascending order  
- button_colors: (Optional) (Ex: blurple,red) Comma separated list of button colors. Valid options: blurple, gray, green, red  
- show_numbers: (Optional) If each option should have a number associated with it when displayed  
- allow_random: (Optional) If a 'random' option is included in the vote  
- force_random: (Optional) If you want to skip the vote altogether and just pick a random option  
- number_of_votes: (Optional) Number of votes per player  
Usage Permissions: Staff Role or Manage Channels Permission  

### /votingmenu remove  
Remove the given voting menu. Usage: /votingmenu remove [title_and_order]  
- title_and_order: (Required) Title and corresponding order of voting menu to delete  
Usage Permissions: Staff Role or Manage Channels Permission

## Webhooks  

Webhooks receive information about a match as it is being setup. Each webhook will contain an "action" key in the payload. Currently supported actions are:  
- JOIN_QUEUE  
- LEAVE_QUEUE  
- MATCH_STARTED  
- TEAMS_CREATED  
- MATCH_COMPLETED  
- SUBSTITUTION  

Additionally, if you have /requireregister mode: Custom API, you will receive a webhook with action REGISTER_PLAYER containing various information about the user, as well as the account they are attempting to register. You must either reply with a json object containing at least a "rating" key (ex: {"rating": 1000}), to specify the rating that the player should be registered with, or any non 200 status response to display to the user.  

### /webhooks add  
Add a new webhook to receive queue information. Usage: /webhooks add [url]  
- url: (Required) Your webhook url  
Usage Permissions: Staff Role or Manage Channels Permission  

### /webhooks delete  
Delete this queue's webhook. Usage: /webhooks delete  
Usage Permissions: Staff Role or Manage Channels Permission  

### /webhooks generatetoken  
Generate an API token for your account. Usage: /webhooks generatetoken  
Usage Permissions: Staff Role or Manage Channels Permission  

## API  
Base URL: https://api.neatqueue.com/
