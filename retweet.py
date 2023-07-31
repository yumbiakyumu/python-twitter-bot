#this is a bot specially created to retweet
#begin with authentication
import tweepy
import time

api_key1 = "xxxxxxxxxxx"
api_secret1 = "xxxxxxxxxxxx"
bearer_token1= r"xxxxxxxxxxxx"
access_token1= "xxxxxxxxxxxxxx"
access_token1_secret="xxxxxxxxxxxx"

client = tweepy.Client(bearer_token1,api_key1,api_secret1,access_token1,access_token1_secret)
auth = tweepy.OAuth1UserHandler(api_key1,api_secret1,access_token1,access_token1_secret)
api = tweepy.API(auth)

class Mystreaam(tweepy.StreamingClient):
     def on_tweet(self, tweet):
          print(tweet.text)

          try:
              client.retweet(tweet.id)

          except Exception as error:
               print(error)

stream = Mystreaam(bearer_token1 = bearer_token1)
#retweet every tweet with SpaceX as the keyword
rule = tweepy.StreamRule("(SpaceX)(-is:retweet -is:reply)")

stream.add_rules(rule)

stream.filter()
