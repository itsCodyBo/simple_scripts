from twython import Twython, TwythonError
import time

#this is the start of the twitter bot, which will tweet one line for me when run

app_key = 'kOWO9eym53xx4KqaPYwu2TFPP'
app_secret = 'odCoTzWoPUYpGhjZ1DuGjeXHKgZP5A3oIC5h52A7OnbiSMDRRv'
oauth_token = '857527369-wwGb79so2nnjCrYaiSdBE4ZCt9lfFtljIMA1VOWJ'
oauth_token_secret = 'UjyeKJyH9WZk5BWm1jRRCzFltaAqUowTtDcjb0R8owOCN'

twitter = Twython(app_key,app_secret,oauth_token,oauth_token_secret)

new_tweet = raw_input("What do you want to tweet? \n")

try:
	twitter.update_status(status=new_tweet)
except TwythonError as e:
	print e

		
