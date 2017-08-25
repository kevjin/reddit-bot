import praw
import os
import time
 
SUB_REDDIT = "jokes"
FRESH_MIN = 300.0 # at least x hours
FRESH_MULTI = 20 #freshness multiplier, hours * fresh_multi is upper bound for score
MAX_SUBMISSIONS = 1000 #maximum submissions

reddit = praw.Reddit("bot1")
subreddit = reddit.subreddit(SUB_REDDIT)

def main():
	print "This is a reddit bot, we have gone into "+ SUB_REDDIT
	old_reposts = get_reposts()
	title, body = search_for_good_post(old_reposts)
	if(submit_repost(title,body)):
		print "You have successfully reposted, now just wait for that sweet karma to flow in."
	else:
		print("Something went wrong :( couldn't repost.")

def get_reposts():
	old_reposts = []
	if os.path.isfile("posts_copied.txt"):
		with open("posts_copied.txt","r") as f:
			old_reposts = f.read()
			old_reposts = old_reposts.split('\n')
	else:
		print("You don't have the reposts file, we will create it for you.")
		with open("posts_copied.txt","w") as f:
			f.write("")
	return old_reposts

def search_for_good_post(old_reposts):

	title = ""
	body = ""

	for submission in subreddit.new(limit=MAX_SUBMISSIONS):
		freshness = (time.time() - submission.created_utc)/(60 * 60) #in terms of hours
		if( freshness > FRESH_MIN):
			if(submission.score > 20 and submission.score < freshness*FRESH_MULTI):
				go_ahead = True
				for repost in old_reposts:
					if repost == submission.title:
						go_ahead = False
				if(go_ahead):
					print("Title: ", submission.title)
					title = submission.title
					print("Body Text: ", submission.selftext)
					body = submission.selftext
					print("--------------------------\n")
					print("This post has " + str(submission.score) + " karma.")
					break
	return title, body
def submit_repost(title, body):
	if(title != ""):
		subreddit.submit(title, selftext = body)
		with open("posts_copied.txt", "w") as f:
			f.write(title + "\n")
		return True
	else:
		print "You need to expand your search parameters, couldn't find anything."
		return False

if __name__ == '__main__':
	main()