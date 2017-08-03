#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#variables that contain the user credentials to access Twitter API
app_key = 'kOWO9eym53xx4KqaPYwu2TFPP'
app_secret = 'odCoTzWoPUYpGhjZ1DuGjeXHKgZP5A3oIC5h52A7OnbiSMDRRv'
oauth_token = '857527369-wwGb79so2nnjCrYaiSdBE4ZCt9lfFtljIMA1VOWJ'
oauth_token_secret = 'UjyeKJyH9WZk5BWm1jRRCzFltaAqUowTtDcjb0R8owOCN'

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
	
	def on_data(self,data):
		print data
		return True
		
	def on_error(self, status):
		print status
	
if __name__ == '__main__':
	
	#This handles Twitter authentification and the connection to Twitter API
	l = StdOutListener()
	auth = OAuthHandler(app_key,app_secret)
	auth.set_access_token(oauth_token,oauth_token_secret)
	stream = Stream(auth, l)	
	
'''this line filter twitter streams to capture data by keywords: python, java, ruby'''
stream.filter(track=['python','java','ruby'])

#import json for reading, pandas for data manipulation and matplotlib for graphical int

import json
import pandas
import matplotlib.pyplot as plt

#read the data into an array that we call tweets.
tweets_data_path = '.../data/twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, 'r')
for line in tweets_file:
	try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
	except:
		continue
