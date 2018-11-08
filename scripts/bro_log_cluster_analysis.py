#!/usr/bin/python

import matplotlib
matplotlib.use('Agg')

# Third Party Imports
import pandas as pd
import sklearn
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

import sys

# Local imports
import bat
from bat import log_to_dataframe
from bat import dataframe_to_matrix


# Pass in bro log
df = log_to_dataframe.LogToDataFrame(sys.argv[1])

df[['request_body_len', 'response_body_len']].hist()
plt.savefig('http_net.png')

plt.gcf().clear()

features = ['id.orig_h', 'id.orig_p', 'id.resp_h', 'id.resp_p', 'orig_pkts', 'resp_pkts']
bro_df = df[features]
# Use the bat DataframeToMatrix class (handles categorical data)
# You can see below it uses a heuristic to detect category data. When doing
# this for real we should explicitly convert before sending to the transformer.
to_matrix = dataframe_to_matrix.DataFrameToMatrix()
bro_matrix = to_matrix.fit_transform(bro_df)

# Just some simple stuff for this example, KMeans and TSNE projection
kmeans = KMeans().fit_predict(bro_matrix)
projection = TSNE().fit_transform(bro_matrix)

# Now we can put our ML results back onto our dataframe!
bro_df['x'] = projection[:, 0] # Projection X Column
bro_df['y'] = projection[:, 1] # Projection Y Column
bro_df['cluster'] = kmeans

# Now use dataframe group by cluster
cluster_groups = bro_df.groupby('cluster')

# Plot the Machine Learning results
fig, ax = plt.subplots()
colors = {0:'red', 1:'orange', 2:'yellow', 3:'green', 4:'blue', 5:'purple', 6:'brown', 7:'black'}
for key, group in cluster_groups:
    group.plot(ax=ax, kind='scatter', x='x', y='y', alpha=0.5, s=250, color=colors[key])

plt.savefig('cluster.png')

# Now print out the details for each cluster
pd.set_option('display.width', 1000)
show_fields = ['id.orig_h', 'id.orig_p', 'id.resp_h', 'id.resp_p', 'orig_pkts', 'resp_pkts']
with open("cluster_file.txt", "w") as fh:
    for key, group in cluster_groups:
        fh.write('\nCluster {:d}: {:d} observations'.format(key, len(group)))
        fh.write(str(group[show_fields].head()))

'''df['uid'].resample('1S').count().plot()
plt.xlabel('Connections Per Second')
plt.savefig('time_series_conns_per_sec.png')'''
