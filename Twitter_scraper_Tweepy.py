# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:44:03 2020

@author: USER
"""
import tweepy
import pandas as pd
import time


# Credentials
consumer_key = "***************"
consumer_secret = "********************"
access_token = "*****************"
access_token_secret = "**********************"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#Function-Query by Username
tweets = []
def username_tweets_to_csv(username,count):
    try: 
    # Pulling individual tweets from query
        for tweet in api.user_timeline(id=username, count=count):

            # Adding to list that contains all tweets
            tweets.append((tweet.created_at,tweet.id,tweet.text))

            # Creation of dataframe from tweets list
            tweetsdf = pd.DataFrame(tweets,columns=['Datetime', 'Tweet Id', 'Text'])

            # Converting dataframe to CSV
            tweetsdf.to_csv('{}-tweets.csv'.format(username)) 

    except BaseException as e:
          print('failed on_status,',str(e))
          time.sleep(3)

#Function-Query by Text Search
tweets = []

def text_query_to_csv(text_query,count):
    try:
    # Pulling individual tweets from query
        for tweet in api.search(q=text_query, count=count):

          # Adding to list that contains all tweets
          tweets.append((tweet.created_at,tweet.id,tweet.text))

          # Creation of dataframe from tweets list
          tweetsdf = pd.DataFrame(tweets,columns=['Datetime', 'Tweet Id', 'Text'])

          # Converting dataframe to CSV
          tweetsdf.to_csv('{}-tweets.csv'.format(text_query)) 

    except BaseException as e:
        print('failed on_status,',str(e))
        time.sleep(3)

#Query by Username
# Input username(s) to scrape tweets and name csv file
# Max recent tweets pulls x amount of most recent tweets from that user
#username = 'CDCgov'
#count = 5000

# Calling function to turn username's past x amount of tweets into a CSV file
#username_tweets_to_csv(username, count)

#Query by Text Search
# Input search query to scrape tweets and name csv file
# Max recent tweets pulls x amount of most recent tweets from that user
text_query = 'Donald Trump'
count = 5000

# Calling function to query X amount of relevant tweets and create a CSV file
text_query_to_csv(text_query, count)









