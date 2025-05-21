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


