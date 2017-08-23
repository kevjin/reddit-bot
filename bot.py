import praw

reddit = praw.Reddit("bot1")

subreddit = reddit.subreddit("learnpython")
print "This is a reddit bot"

for submission in subreddit.hot(limit=5):
	print("Title: ", submission.title)
	print("Score: ", submission.selftext)
	print("--------------------------\n")