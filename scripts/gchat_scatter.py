#!/usr/bin/python

import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import pandas as pd
import scattertext as st
import spacy
import matplotlib.dates as mdates
from datetime import datetime
from wordcloud import WordCloud

dflst = []

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
d = {'author_chat_id':'108778762612058411235', 'author_name':'John Macron', 'timestamp':'2017-07-17 15:04:12', 'text':'t&#39;s too late now! U promised'}
dflst.append(d)
d = {'author_chat_id':'112549252980293459976', 'author_name':'Hallym Betty', 'timestamp':'2017-07-17 15:04:18', 'text':'Evwryone suspectbs'}
dflst.append(d)
d = {'author_chat_id':'112549252980293459976', 'author_name':'Hallym Betty', 'timestamp':'2017-07-17 15:04:36', 'text':'Tt feels like they are warching us'}
dflst.append(d)
d = {'author_chat_id':'108778762612058411235', 'author_name':'John Macron', 'timestamp':'2017-07-17 15:04:45', 'text':'t&#39;s too late now! U promised'}
dflst.append(d)
d = {'author_chat_id':'112549252980293459976', 'author_name':'Hallym Betty', 'timestamp':'2017-07-17 15:05:09', 'text':'I cannot take it anymore'}
dflst.append(d)
d = {'author_chat_id':'108778762612058411235', 'author_name':'John Macron', 'timestamp':'2017-07-17 15:05:22', 'text':'...'}
dflst.append(d)
d = {'author_chat_id':'112549252980293459976', 'author_name':'Hallym Betty', 'timestamp':'2017-07-17 15:05:25', 'text':'Its over dont msg me'}
dflst.append(d)
d = {'author_chat_id':'108778762612058411235', 'author_name':'John Macron', 'timestamp':'2017-07-17 15:05:40', 'text':'Who the fuck do you think k you are!'}
dflst.append(d)

df = pd.DataFrame(dflst)

df['text_length'] = df['text'].apply(len)

for 
# Create the base line
start = min(dates)
stop = max(dates)
ax.plot((start, stop), (0, 0), 'k', alpha=.5)

names = df['author_name'].tolist()
dates = [datetime.strptime(ii, "%Y-%m-%d %H:%M:%S") for ii in df['timestamp']]

# Iterate through releases annotating each one
for ii, (iname, idate) in enumerate(zip(names, dates)):
    


plt.scatter(x,y)
plt.savefig('chat_scatter.png')
