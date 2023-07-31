# Import the required libraries
import tweepy
import time

# Replace "xxxxxxxxxxx", "xxxxxxxxxxxx", "xxxxxxxxxxxx", "xxxxxxxxxxxxxx", and "xxxxxxxxxxxx" with your actual API credentials
api_key1 = "xxxxxxxxxxx"
api_secret1 = "xxxxxxxxxxxx"
bearer_token1 = r"xxxxxxxxxxxx"
access_token1 = "xxxxxxxxxxxxxx"
access_token1_secret = "xxxxxxxxxxxx"

# Authenticate with Twitter API using the provided credentials
client = tweepy.Client(bearer_token1, api_key1, api_secret1, access_token1, access_token1_secret)
auth = tweepy.OAuth1UserHandler(api_key1, api_secret1, access_token1, access_token1_secret)
api = tweepy.API(auth)

# Create a class named Mystreaam, inheriting from tweepy.StreamingClient
class Mystreaam(tweepy.StreamingClient):

    # Override the on_tweet method, which is called when a new tweet is received
    def on_tweet(self, tweet):
        print(tweet.text)  # Print the text of the received tweet

        try:
            # Retweet the tweet with the given tweet ID
            client.retweet(tweet.id)

        except Exception as error:
            print(error)

# Create an instance of the custom streaming class Mystreaam with the bearer token
stream = Mystreaam(bearer_token1=bearer_token1)

# Define a rule to filter tweets containing "SpaceX" as the keyword but excluding retweets and replies
rule = tweepy.StreamRule("(SpaceX)(-is:retweet -is:reply)")

# Add the rule to the streaming instance
stream.add_rules(rule)

# Start filtering tweets based on the defined rule and retweeting them
stream.filter()
