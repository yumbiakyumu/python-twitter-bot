import tweepy

api_key1 = "xxxxxxxxxx"
api_secret1 = "xxxxxxxxxxx"
bearer_token1= r"xxxxxxxxxxxx"
access_token1= "xxxxxxxxxxxxxx"
access_token1_secret="xxxxxxxxxxx"

client = tweepy.Client(bearer_token1,api_key1,api_secret1,access_token1,access_token1_secret)
auth = tweepy.OAuth1UserHandler(api_key1,api_secret1,access_token1,access_token1_secret)
api = tweepy.API(auth)

# client.create_tweet(text = "testing twiiter bot")
#client.like("1683177901431062528")
#client.retweet("1683177901431062528")
#client.create_tweet(in_reply_to_tweet_id="1683177901431062528" , text = "ok it works" )
#for tweet in api.home_timeline():print(tweet.text)
person = client.get_user(username ="elonmusk").data.id
#run a for loop to print all for loops present in the usernames timelines
for tweet in client.get_users_tweets(person).data:print(tweet.text)
