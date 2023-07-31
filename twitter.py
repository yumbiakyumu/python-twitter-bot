# Import the tweepy library, which provides a wrapper for the Twitter API
import tweepy

# Replace "xxxxxxxxxx", "xxxxxxxxxxx", "xxxxxxxxxxxx", "xxxxxxxxxxxxxx", and "xxxxxxxxxxx" with your actual API credentials
api_key1 = "xxxxxxxxxx"
api_secret1 = "xxxxxxxxxxx"
bearer_token1 = r"xxxxxxxxxxxx"
access_token1 = "xxxxxxxxxxxxxx"
access_token1_secret = "xxxxxxxxxxx"

# Create a 'client' object using the provided credentials to authenticate API requests
client = tweepy.Client(bearer_token1, api_key1, api_secret1, access_token1, access_token1_secret)

# Create an 'auth' object using OAuth1UserHandler with the provided API credentials and access tokens
auth = tweepy.OAuth1UserHandler(api_key1, api_secret1, access_token1, access_token1_secret)

# Create an 'api' object using the 'auth' object to access the Twitter API with authenticated privileges
api = tweepy.API(auth)

# The following actions are currently commented out (using '#'), meaning they will not be executed:

# Create a tweet with the specified text (currently commented out)
# client.create_tweet(text="testing twitter bot")

# Like (i.e., favorite) the tweet with the given tweet ID (currently commented out)
# client.like("1683177901431062528")

# Retweet the tweet with the given tweet ID (currently commented out)
# client.retweet("1683177901431062528")

# Create a reply tweet to the tweet with the specified ID (currently commented out)
# client.create_tweet(in_reply_to_tweet_id="1683177901431062528", text="ok it works")

# Loop through and print the text of tweets on the user's home timeline (currently commented out)
# for tweet in api.home_timeline():
#     print(tweet.text)

# Fetch the user ID of "elonmusk" using the 'client.get_user' method and store it in the 'person' variable
person = client.get_user(username="elonmusk").data.id

# Run a for loop to print the text of all tweets present in the timelines of the user with the 'person' ID
for tweet in client.get_users_tweets(person).data:
    print(tweet.text)
