# Data Science Twitter Text Sentiment Classification: Project Overview 
* Created a tool that identifies data science Twitter text sentiment to help candidate or company notice popularity, and brand awareness.  
* Scraped about 10000 tweets from Twitter using python, tweepy, and GetOldTweets3  
* Analyzed Sentiment using vaderSentiment.  

## Code and Resources Used
**Python Version:** 3.7  
**Packages:** pandas, matplotlib, seaborn, tweepy, GetOldTweets3, langdetect, vaderSentiment  
**Scraper Github:** https://github.com/MartinBeckUT/TwitterBot/tree/master/TwitterScraper  
**Scraper Article:** https://towardsdatascience.com/how-to-scrape-tweets-from-twitter-59287e20f0f1  
**Analysis Github:** https://github.com/PlayingNumbers/Captain_Marvel_Sentiment/blob/master/sentiment_a.py  

## Web Scraping
Tweaked the web scraper github repo (above) to scrape 10000 tweets from Twitter.com. I collected USA Presidential Candidate--Donald Trump in 2016 and 2020, I got the following:
* Datetime
* Text

## Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:
* Add column for detecting the language of tweets is english or not. 

## Sentiment Analysis
I scarped the tweets that talk about Donald Trump in 2016 and 2020 and analyzed. Below are a few highlights from the result.
According to the picture, we can see the positive tweets higher than negative tweets in 2016:  
![](https://github.com/ILing82816/ds_twitter_sentiment_proj/blob/master/2016_Trump.png)  
According to the picture, we can see the negative tweets higher than positive tweets in 2020:  
![](https://github.com/ILing82816/ds_twitter_sentiment_proj/blob/master/2020_Trump.png)  
We can say Donald Trump did some wrong policies or said something that people didn't like during four years. Hence, he is hard to continue in office.  
![](https://github.com/ILing82816/ds_twitter_sentiment_proj/blob/master/Compare.png)  
