#!/usr/bin/python                                                                                                    
import matplotlib
matplotlib.use('Agg')


import nltk.data
import nltk
nltk.download('vader_lexicon')
nltk.download('opinion_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize
from nltk.corpus import opinion_lexicon
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import pandas as pd

dflst = []

# prepare for claculate word frequencies
positive = set(opinion_lexicon.positive())
negative = set(opinion_lexicon.negative())

# Create DF sentiment analysis
d = {'author_chat_id':'108778762612058411235', 'author_name':'John Macron', 'timestamp':'2017-07-17 13:39:08', 'text':';)'}         
dflst.append(d)
d = {'author_chat_id':'108778762612058411235', 'author_name':'John Macron', 'timestamp':'2017-07-17 13:41:54', 'text':'How are you?'}
dflst.append(d)
d = {'author_chat_id':'112549252980293459976', 'author_name':'Hallym Betty', 'timestamp':'2017-07-17 13:43:21', 'text':'Hey. Better now ;)'}         
dflst.append(d)
d = {'author_chat_id':'108778762612058411235', 'author_name':'John Macron', 'timestamp':'2017-07-17 13:47:12', 'text':'Ugh. Work sucks'}
dflst.append(d)
d = {'author_chat_id':'108778762612058411235', 'author_name':'John Macron', 'timestamp':'2017-07-17 13:47:17', 'text':'I wanna see you later'}
dflst.append(d)
d = {'author_chat_id':'112549252980293459976', 'author_name':'Hallym Betty', 'timestamp':'2017-07-17 15:03:45', 'text':'I cant keep doing this'}
dflst.append(d)
d = {'author_chat_id':'108778762612058411235', 'author_name':'John
Macron', 'timestamp':'2017-07-17 15:04:12', 'text':'t&#39;s too late
now! U promised'} dflst.append(d)
d = {'author_chat_id':'112549252980293459976', 'author_name':'Hallym Betty', 'timestamp':'2017-07-17 15:04:18', 'text':'Evwryone suspectbs'}
dflst.append(d)
d = {'author_chat_id':'112549252980293459976', 'author_name':'Hallym Betty', 'timestamp':'2017-07-17 15:04:36', 'text':'t feels like they are warching us'}
dflst.append(d)
d = {'author_chat_id':'108778762612058411235', 'author_name':'John
Macron', 'timestamp':'2017-07-17 15:04:12', 'text':'t&#39;s too late
now! U promised'} dflst.append(d)




df = pd.DataFrame(dflst)

'''df['positive'] = df.text.apply(lambda x: len(positive.intersection(x)))
df['negative'] = df.text.apply(lambda x: len(negative.intersection(x)))
df['sentiment'] = df.positive - df.negative

newdf = df[['author_name', 'text', 'positive', 'negative', 'sentiment', 'timestamp']]
print(df.describe())'''

# Next, we initialize VADER so we can use it within our Python script
sid = SentimentIntensityAnalyzer()

summary = {"positive":0, "neutral":0, "negative":0}
for item in df['text']:
    if ":" in item:
        print(item)
        scores = sid.polarity_scores(item)     
        for key in sorted(scores):
            print('{0}: {1}, '.format(key, scores[key]))
            if scores["compound"] == 0.0:
                summary["neutral"] += 1
            elif scores["compound"] > 0.0:
                summary["positive"] += 1
            else:
                summary["negative"] += 1

print(summary)
#plt.bar(summary.keys(), summary.values())
#plt.savefig("sentiment_analysis.png")'''

