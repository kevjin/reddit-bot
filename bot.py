import praw
import pdb
import re #regular expressions
import os
import json
import requests
import time

SUB_REDDIT = "jokes"
FRESH_MIN = 30.0 # at least x hours
FRESH_MULTI = 20
reddit = praw.Reddit("bot1")
subreddit = reddit.subreddit(SUB_REDDIT)
print "This is a reddit bot, we have gone into "+ SUB_REDDIT
title = ""
body = ""
for submission in subreddit.new(limit=1000):
	freshness = (time.time() - submission.created_utc)/(60 * 60) #in terms of hours
	if( freshness > FRESH_MIN):
		if(submission.score > 20 and submission.score < freshness*FRESH_MULTI):
			print("Title: ", submission.title)
			title = submission.title
			print("Body Text: ", submission.selftext)
			body = submission.selftext
			print("--------------------------\n")
			with open("posts_copied.txt", "w") as f:
				f.write(submission.title + "\n")
			break

if(title != ""):
	subreddit.submit(title, selftext = body)
	print "You have successfully reposted, now just wait for that sweet karma to flow in."
else:
	print "You need to expand the parameters, couldn't find anything."


'''if not os.path.isfile("posts_replied_to.txt"):
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
		f.write(post_id + "\n")'''
