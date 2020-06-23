# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:44:03 2020

@author: USER
"""
import pandas as pd 
import datetime as dt 
from twitterscraper import query_tweets
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#from langdetect import detect 


#def detector(x):
#    try:
#       return detect(x)
#    except:
#        None 

#Build Analyzer Object        
#analyzer = SentimentIntensityAnalyzer()

#Trade War - 2018
begin_date_one = dt.date(2018,3,22)
end_date_one = dt.date(2018,4,20)
begin_date_two = dt.date(2018,5,29)
end_date_two = dt.date(2018,9,24)


#query tweets with our parameters
tweets_one = query_tweets("#TradeWar", begindate = begin_date_one, enddate= end_date_one, limit = 1000, lang= "english")
tweets_two = query_tweets("#TradeWar", begindate = begin_date_two, enddate = end_date_two, limit = 1000, lang= "english")

#covert to dataframe                         
df_one = pd.DataFrame(t.__dict__ for t in tweets_one)
df_two = pd.DataFrame(t.__dict__ for t in tweets_two)

#filter for english tweets
#df_one['lang'] = df_one['text'].apply(lambda x:detector(x))
#df_one = df_one[df_one['lang'] == 'en']
#df_two['lang'] = df_two['text'].apply(lambda x: detector(x))
#df_two = df_two[df_two['lang'] == 'en'] 

#save files
df_one.to_csv('tw2018one_tweets_before_clean.csv')
df_two.to_csv('tw2018two_tweets_after_clean.csv')


