# Repost Bot #

*Note: This bot is still a work in progress.* The purpose of this bot is to generate as much post karma as it can (karma is a point system on reddit that users acquire through recieving 'upvotes' or 'likes' on their posts and comments from other users. Karma is cumulative across upvotes from different posts. The bot searches for older reddit posts with at least a certain amount of karma and other specific parameters, and 'reposts' it. The bot submits the same title text and post text as the original author.


## How to use the bot ##

*Assumes a basic understanding of Reddit*

In the praw.ini file, replace the "REDACTED" text with their respected values. You can get the client_id and client_secret from https://ssl.reddit.com/prefs/apps and scrolling to the bottom to 'create another app'.
1). Give a name for your bot
2). Choose the 'script' radio button.
3). Set the redirect_uri to '127.0.0.1' *This is more for web apps, but reddit api still requires a value for your python script*

Retrieve the client_id and client_secret from your newly created application and set the respective variables in praw.ini with these.

The username and password variables are your reddit bot's username and password. Create a new reddit account for your bot, and pass on the username and password to these variables.

user_agent is a unique identifier for the reddit api to know who your bot is. It can be something like 'repost-bot v.01' or whatever unique.

## Tips ##

Before reposting on subreddits, make sure to check whether the subreddit allows reposts or not. Also some subreddits require a minimum amount of karma, subscription, or account age before you can post on them. Make sure to choose a subreddit that your bot can safely post to, without having your post being removed/filtered automatically.

Have fun! :)
-kevjin
