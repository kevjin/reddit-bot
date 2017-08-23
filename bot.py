import praw
import pdb
import re #regular expressions
import os

SUB_REDDIT = "pythonforengineers"
reddit = praw.Reddit("bot1")
SUB_REDDIT
subreddit = reddit.subreddit(SUB_REDDIT)
print "This is a reddit bot, we have gone into "+ SUB_REDDIT

'''for submission in subreddit.hot(limit=5):
	print("Title: ", submission.title)
	print("Score: ", submission.selftext)
	print("--------------------------\n")'''

if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []
else:
	with open("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None,posts_replied_to))
for submission in subreddit.hot(limit=2): #up to 5 submissions
	if submission.id not in posts_replied_to:
		if re.search("I love python", submission.title, re.IGNORECASE):
			submission.reply("OMGG I love python too(.7)! XD")
		posts_replied_to.append(submission.id)
with open("posts_replied_to.txt", "w") as f:
	for post_id in posts_replied_to:
		f.write(post_id + "\n")
