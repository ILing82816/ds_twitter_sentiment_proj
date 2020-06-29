# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:18:36 2020

@author: USER
"""
import pandas as pd
from langdetect import detect
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#Data preparation
def detector(x):
    try:
       return detect(x)
    except:
        None 
        
df_2016 = pd.read_csv('Donald Trump-2016-01-01-tweets.csv')
df_2016['lang'] = df_2016['Text'].apply(lambda x:detector(x))
df_2016 = df_2016[df_2016['lang'] == 'en']

df_2020 = pd.read_csv('Donald Trump-2020-01-01-tweets.csv')
df_2020['lang'] = df_2020['Text'].apply(lambda x:detector(x))
df_2020 = df_2020[df_2020['lang'] == 'en']


#Data EDA
words = " ".join(df_2016['Text'])
def punctuation_stop(text):
    filtered = []
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    for w in word_tokens:
        if w not in stop_words and w.isalpha():
            filtered.append(w.lower())
    return filtered
words_filtered = punctuation_stop(words)

text = " ".join([ele for ele in words_filtered])

wc= WordCloud(background_color="white", random_state=1,stopwords=STOPWORDS, max_words = 2000, width =800, height = 1500)
wc.generate(text)

plt.figure(figsize=[10,10])
plt.imshow(wc,interpolation="bilinear")
plt.axis('off')
plt.show()


words = " ".join(df_2020['Text'])
def punctuation_stop(text):
    filtered = []
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    for w in word_tokens:
        if w not in stop_words and w.isalpha():
            filtered.append(w.lower())
    return filtered
words_filtered = punctuation_stop(words)

text = " ".join([ele for ele in words_filtered])

wc= WordCloud(background_color="white", random_state=1,stopwords=STOPWORDS, max_words = 2000, width =800, height = 1500)
wc.generate(text)

plt.figure(figsize=[10,10])
plt.imshow(wc,interpolation="bilinear")
plt.axis('off')
plt.show()




#Analyzer
analyzer = SentimentIntensityAnalyzer()
#get sentiment scores
sentiment_2016 = df_2016['Text'].apply(lambda x: analyzer.polarity_scores(x))
sentiment_2020 = df_2020['Text'].apply(lambda x: analyzer.polarity_scores(x))
#put sentiment into dataframe
df_2016 = pd.concat([df_2016, sentiment_2016.apply(pd.Series)],1)
df_2020 = pd.concat([df_2020, sentiment_2020.apply(pd.Series)],1)

df_2016_nz = df_2016[df_2016['compound'] != 0]
df_2020_nz = df_2020[df_2020['compound'] != 0]
#Result
df_2016_nz['compound'].sample(5000).hist()
plt.title('2016 USA Presidential candidate--Donald Trump')
plt.show()

df_2020_nz['compound'].sample(5000).hist()
plt.title('2020 USA Presidential candidate--Donald Trump')
plt.show()

ax1 = sns.distplot(df_2016_nz['compound'], bins=15, hist = False, label = '2016 year', color ='blue',  kde_kws={'linestyle':'--'})
ax2 = sns.distplot(df_2020_nz['compound'], bins=15, hist = False, label = '2020 year', color ='blue')
plt.legend()
plt.title('2016 vs. 2020 USA Presidential candidate--Donald Trump')
plt.show()
