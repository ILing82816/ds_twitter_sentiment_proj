# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:12:56 2020

@author: USER
"""
import GetOldTweets3 as got
import pandas as pd

#Function-Query by Username
# Function the pulls tweets from a specific username and turns to csv file

# Parameters: (list of twitter usernames), (max number of most recent tweets to pull from)
def username_tweets_to_csv(username, count):
    # Creation of query object
    tweetCriteria = got.manager.TweetCriteria().setUsername(username)\
                                            .setMaxTweets(count)
    # Creation of list that contains all tweets
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    # Creating list of chosen tweet data
    user_tweets = [[tweet.date, tweet.text] for tweet in tweets]

    # Creation of dataframe from tweets list
    tweets_df = pd.DataFrame(user_tweets, columns = ['Datetime', 'Text'])

    # Converting dataframe to CSV
    tweets_df.to_csv('{}-{}k-tweets.csv'.format(username, int(count/1000)), sep=',')

#Function-Query by Text Search
# Function that pulls tweets based on a general search query and turns to csv file

# Parameters: (text query you want to search), (max number of most recent tweets to pull from)
def text_query_to_csv(text_query, count):
    # Creation of query object
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(text_query)\
                                                .setSince(since_date).setUntil(until_date).setMaxTweets(count)
    # Creation of list that contains all tweets
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    # Creating list of chosen tweet data
    text_tweets = [[tweet.date, tweet.text] for tweet in tweets]

    # Creation of dataframe from tweets
    tweets_df = pd.DataFrame(text_tweets, columns = ['Datetime', 'Text'])

    # Converting tweets dataframe to csv file
    tweets_df.to_csv('{}-{}k-tweets.csv'.format(text_query, int(count/1000)), sep=',')

#Query by Username

#Query by Text Search
# Input search query to scrape tweets and name csv file
# Max recent tweets pulls x amount of most recent tweets from that user
text_query = 'Trade War'
since_date = '2018-03-01'
until_date = '2019-10-31'
count = 10000

# Calling function to query X amount of relevant tweets and create a CSV file
text_query_to_csv(text_query, count)