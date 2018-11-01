#!/usr/bin/python                                                                                                    
import matplotlib
matplotlib.use('Agg')


import nltk.data
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize
import numpy as np
import matplotlib.pyplot as plt

import sys
import pandas as pd


# Convert CSV to Pandas Dataframe
df = pd.read_csv(sys.argv[1])

# Next, we initialize VADER so we can use it within our Python script
sid = SentimentIntensityAnalyzer()

summary = {"positive":0, "neutral":0, "negative":0}
for item in df['notes']:
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
        
plt.bar(summary.keys(), summary.values())
plt.savefig("sentiment_analysis.png")

