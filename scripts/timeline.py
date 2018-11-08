#!/usr/bin/python

from collections import Counter, defaultdict, OrderedDict
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

names = ['Simon', 'Simon', 'Kore', 'dp', 'Simon', 'Simon', 'dp', 'Unknown', 'Unknown', 'dp', 'dp', 'Kore', 'Simon', 'Betty', 'Simon', 'Betty', 'Kore', 'Unknown', 'Unknown', 'Simon', 'Kore', 'Betty', 'Examiner']
dates = ['2017-07-16 17:14:43', '2017-07-16 17:14:43', '2017-07-16 17:18:49', '2017-07-16 17:57:44', '2017-07-16 19:59:12', '2017-07-16 19:59:12', '2017-07-16 20:11:46', '2017-07-17 13:41:26', '2017-07-17 13:44:48', '2017-07-17 14:13:37','2017-07-17 14:16:13', '2017-07-17 14:18:44', '2017-07-17 14:21:48', '2017-07-17 14:22:12', '2017-07-17 15:00:45', '2017-07-17 15:00:46', '2017-07-17 15:02:05', '2017-07-17 15:11:55','2017-07-17 15:15:21', '2017-07-17 15:20:50', '2017-07-17 15:25:21', '2017-07-17 16:21:35', '2017-07-17 16:27:57']

dates = [datetime.strptime(ii, "%Y-%m-%d %H:%M:%S") for ii in dates]

levels = np.array([-10, 10, -9, 9, -8, 8, -6, 6, -4, 4, -2, 2])
fig, ax = plt.subplots()

# Create the base line
start = min(dates)
stop = max(dates)
ax.plot((start, stop), (0, 0), 'k', alpha=.5)

# Iterate through releases annotating each one
for ii, (iname, idate) in enumerate(zip(names, dates)):
    level = levels[ii % 10]
    vert = 'top' if level < 0 else 'bottom'
    ax.scatter(idate, 0, s=100, facecolor='w', edgecolor='k', zorder=9999)
    # Plot a line up to the text
    ax.plot((idate, idate), (0, level), c='r', alpha=.7)
    # Give the text a faint background and align it properly
    ax.text(idate, level, iname, horizontalalignment='right', verticalalignment=vert, fontsize=8, backgroundcolor=(1., 1., 1., .3))

ax.set(title="Device Time Analysis")
# Set the xticks formatting
# format xaxis with 3 month intervals
ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=3))
ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
fig.autofmt_xdate()

# Remove components for a cleaner look
plt.setp((ax.get_yticklabels() + ax.get_yticklines() +
                    list(ax.spines.values())), visible=False)
plt.savefig('timeline.png')


plt.gcf().clear()

z = Counter(names)
labels = z.keys()
plt.bar(range(len(z)), list(z.values()))
plt.xticks(range(len(labels)), labels, rotation='vertical')
plt.xlabel("Device Name")
plt.ylabel("Number of Connections")
plt.title("The Number of Connections Per Device")
plt.legend()
plt.savefig("device_counts.png")
