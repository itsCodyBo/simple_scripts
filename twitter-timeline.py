#Download home timeline tweets and print each one on console
#link to guide: http://tweepy.readthedocs.io/en/v3.5.0/getting_started.html
#go to apps.twitter.com and login for auth and token keys

import tweepy

#authenticate with your twitter application (located at apps.twitter.com)
auth=tweepy.OAuthHandler('Rq7KMaDVbEB3bKIWwesfDgQLV','uaNOtzLv17v5jZ1QRreAZ2vjG6oz5I0XVZvSL7h4iE4x9yuXTi')
auth.set_access_token('857527369-OgjAJ9eaD9FmntDLZSxIYv9J3KlIIrymzwqjHuXT','kNUCyeR8MdCqXX9Ok90yHQ9CjlErPCLYcquYFHKOFLnjG')

#start the instance I think (?)
api = tweepy.API(auth)

#grab the public timeline tweets
public_tweets = api.home_timeline()
for tweet in public_tweets:
	print tweet.text
