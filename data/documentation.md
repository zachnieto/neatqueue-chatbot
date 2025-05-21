# Quick start
Starting a queue is super simple with NeatQueue, just run one of the following commands:
- /setup for an interactive walk through
- /startqueue for a simple default configuration
- /load [config_id] for a specific queue configuration

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
