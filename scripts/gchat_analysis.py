#!/usr/bin/python

import textmining
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

wordcloud = WordCloud().generate(' '.join(df['text'].tolist()))
plt.savefig('wordcloud.png')

names = df['author_name'].tolist()
dates = [datetime.strptime(ii, "%Y-%m-%d %H:%M:%S") for ii in df['timestamp']]

levels = np.array([-10, 10, -8, 8, -6, 6, -4, 4, -2, 2])
fig, ax = plt.subplots(figsize=(8, 5))

# Create the base line
start = min(dates)
stop = max(dates)
ax.plot((start, stop), (0, 0), 'k', alpha=.5)

# Iterate through releases annotating each one
for ii, (iname, idate) in enumerate(zip(names, dates)):
    level = levels[ii % 6]
    vert = 'top' if level < 0 else 'bottom'
    ax.scatter(idate, 0, s=100, facecolor='w', edgecolor='k', zorder=9999)
    # Plot a line up to the text
    ax.plot((idate, idate), (0, level), c='r', alpha=.7)
    # Give the text a faint background and align it properly
    ax.text(idate, level, iname, horizontalalignment='right', verticalalignment=vert, fontsize=10, backgroundcolor=(1., 1., 1., .3))

ax.set(title="Google Chat Time Analysis")
# Set the xticks formatting
# format xaxis with 3 month intervals
ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=3))
ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
fig.autofmt_xdate()

# Remove components for a cleaner look
plt.setp((ax.get_yticklabels() + ax.get_yticklines() +
                    list(ax.spines.values())), visible=False)
plt.savefig('chat_timeline.png')

# tdm = textmining.TermDocumentMatrix()
word = ''
# john = '' 
for index, row in df.iterrows():
        word += str(row['text']) + " "
   
# tdm.add_doc(betty)
# tdm.add_doc(john)
numLen = len(word.split(" "))

# ax = sns.heatmap(tdm)
