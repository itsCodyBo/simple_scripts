from twython import Twython, TwythonError


APP_KEY = 'kOWO9eym53xx4KqaPYwu2TFPP'
APP_SECRET = 'odCoTzWoPUYpGhjZ1DuGjeXHKgZP5A3oIC5h52A7OnbiSMDRRv'
OAUTH_TOKEN = '857527369-wwGb79so2nnjCrYaiSdBE4ZCt9lfFtljIMA1VOWJ'
OAUTH_TOKEN_SECRET = 'UjyeKJyH9WZk5BWm1jRRCzFltaAqUowTtDcjb0R8owOCN'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
    twitter.update_status(status='Hello World!')
except TwythonError as e:
    print e
