#This bo will get all tweets with a paticular hashtag and like them 
import tweepy
import time

api_key1 = "xxxxxxxx"
api_secret1 = "xxxxxxxxxxx"
bearer_token1= r"xxxxxxxxxxxxx"
access_token1= "xxxxxxxxxxxxxxx"
access_token1_secret="xxxxxxxxxxxxxxxx"

client = tweepy.Client(bearer_token1,api_key1,api_secret1,access_token1,access_token1_secret)
auth = tweepy.OAuth1UserHandler(api_key1,api_secret1,access_token1,access_token1_secret)
api = tweepy.API(auth)

class MiStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        
        try:
              client.like(tweet.id)

        except Exception as error:
               print(error)

        time.sleep(1)

stream = MiStream(bearer_token1 = bearer_token1)
#like every tweet with SpaceX as the keyword
rule = tweepy.StreamRule("(SpaceX OR #starlink)(-is:retweet -is:reply)")
stream.add_rules(rule)

stream.filter()