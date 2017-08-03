'''
Created on Apr 1, 2016

@author: cody
'''
from twython import Twython

APP_KEY = 'kOWO9eym53xx4KqaPYwu2TFPP'
APP_SECRET = 'odCoTzWoPUYpGhjZ1DuGjeXHKgZP5A3oIC5h52A7OnbiSMDRRv'
OAUTH_TOKEN = '857527369-wwGb79so2nnjCrYaiSdBE4ZCt9lfFtljIMA1VOWJ'
OAUTH_TOKEN_SECRET = 'UjyeKJyH9WZk5BWm1jRRCzFltaAqUowTtDcjb0R8owOCN'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

user_timeline = twitter.get_user_timeline(screen_name="wodeyd")

for tweet in user_timeline:
    print tweet['text']