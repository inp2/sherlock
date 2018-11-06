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

from collections import Counter

dflst = []

# Create DF sentiment analysis
d = {'text':'alexa kinda patton a.m. next monday'}         
dflst.append(d)
d = {'text':'alexa'}
dflst.append(d)
d = {'text':'wake up'}
dflst.append(d)
d = {'text':'alexa stop'}
dflst.append(d)
d = {'text':'alexa'}
dflst.append(d)
d = {'text':'turn on tv'}
dflst.append(d)
d = {'text':'alexa'}
dflst.append(d)
d = {'text':'turn on pandora'}
dflst.append(d)
d = {'text':'alexa how could you do this what are the flooding'}
dflst.append(d)
d = {'text':'alexa'}
dflst.append(d)
d = {'text':'stop'}
dflst.append(d)
d = {'text':'alex'}
dflst.append(d)
d = {'text': 'turn off tv'}
dflst.append(d)
d = {'text': 'alexa'}
dflst.append(d)
d = {'text': 'who yes'}
dflst.append(d)

df = pd.DataFrame(dflst)

lst = []

for item in df['text']:
    lst.extend(item.split(" "))

counts = Counter(lst)
print(counts)


'''names = df['author_name'].tolist()
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

# ax = sns.heatmap(tdm)'''
