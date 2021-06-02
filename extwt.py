import re
import io
import tweepy
import time
from tweepy import OAuthHandler

# keys removed for safety purposes.
consumer_key = 'XXXXX'
consumer_secret = 'XXXXX'
access_token = 'XXXXX'
access_token_secret = 'XXXXX'

# create OAuthHandler object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set access token and secret
auth.set_access_token(access_token, access_token_secret)
# create tweepy API object to fetch tweets
api = tweepy.API(auth)


def get_tweets(query, count):

    # empty list to store parsed tweets
    tweets = []
    target = io.open("tweets.txt", 'a+', encoding='utf-8')
    # call twitter api to fetch tweets
    q=str(query)
    fetched_tweets = api.search(q, count = count, tweet_mode="extended")
    # parsing tweets one by one
    print(len(fetched_tweets))

    for tweet in fetched_tweets:
        # print(tweet)


        # empty dictionary to store required params of a tweet
        parsed_tweet = {}
        # saving text of tweet
# use tweet.full_text to obtain the full length tweet.
        parsed_tweet['text'] = tweet.full_text
        if "http" not in tweet.full_text:
            #filter language
            if tweet.lang == "en":
                try:
                    message = tweet.retweeted_status.full_text
                except AttributeError:  # Not a Retweet
                    message = tweet.full_text
#removes the text 'RT' since it was the most common text phrase
                message = message.replace("RT ", "")

                target.write(message+"\n")
    return tweets

#looping a request of 100 tweets at a time due to Twitter restrictions and
# account blocking
i = 0
while (i<10):
    # Change this to what you want to query the tweets
    tweets = get_tweets("covid", 100)
#sleep so that twitter doesnt block the account
    time.sleep(20)
#line between each loop
    print("________")
    i= i +1
print("Done!")
