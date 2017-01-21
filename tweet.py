import  oauth2 as oauth
import json

CONSUMER_KEY = "Qo5vnZvAa6QgERRGc2tpKJvMJ"
CONSUMER_SECRET = "lezQhhbw4T0jwUFar0xQtEku7m1madxfYaSpNZ713Xzpjhlx7C"
ACCESS_KEY = "811594720501780480-XVs830FK8EvIho9zvZgZVJ0XzDv3Jv5"
ACCESS_SECRET = "epOqh3JP3VdxkE2ptUXfpmezyPnLkD1GfQZAPRmgRqBLa"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

name= raw_input("enter user name:\n")
timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+name+"&count=20"
response, data = client.request(timeline_endpoint)
print "\nTweets of ",name,"\n"
tweets = json.loads(data)
for tweet in tweets:
    print tweet['text']
