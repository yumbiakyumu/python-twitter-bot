# Import the required libraries
import tweepy
import time

# Replace "xxxxxxxx", "xxxxxxxxxxx", "xxxxxxxxxxxxx", "xxxxxxxxxxxxxxx", and "xxxxxxxxxxxxxxxx" with your actual API credentials
api_key1 = "xxxxxxxx"
api_secret1 = "xxxxxxxxxxx"
bearer_token1 = r"xxxxxxxxxxxxx"
access_token1 = "xxxxxxxxxxxxxxx"
access_token1_secret = "xxxxxxxxxxxxxxxx"

# Authenticate with Twitter API using the provided credentials
client = tweepy.Client(bearer_token1, api_key1, api_secret1, access_token1, access_token1_secret)
auth = tweepy.OAuth1UserHandler(api_key1, api_secret1, access_token1, access_token1_secret)
api = tweepy.API(auth)

# Create a class named MiStream, inheriting from tweepy.StreamingClient
class MiStream(tweepy.StreamingClient):

    # Override the on_tweet method, which is called when a new tweet is received
    def on_tweet(self, tweet):
        print(tweet.text)  # Print the text of the received tweet

        try:
            # Like (i.e., favorite) the tweet with the given tweet ID
            client.like(tweet.id)

        except Exception as error:
            print(error)

        # Pause the execution for 1 second to avoid excessive liking
        time.sleep(1)

# Create an instance of the custom streaming class MiStream with the bearer token
stream = MiStream(bearer_token1=bearer_token1)

# Define a rule to filter tweets containing "SpaceX" or "#starlink" as the keyword but excluding retweets and replies
rule = tweepy.StreamRule("(SpaceX OR #starlink)(-is:retweet -is:reply)")

# Add the rule to the streaming instance
stream.add_rules(rule)

# Start filtering tweets based on the defined rule and liking them
stream.filter()
