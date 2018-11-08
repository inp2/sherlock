#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')

import sys
import socket

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import pygraphviz as pgv

from bat.log_to_dataframe import LogToDataFrame
from networkx.drawing.nx_pydot import write_dot
from networkx.drawing.nx_agraph import graphviz_layout


df = LogToDataFrame(sys.argv[1])

features = ['id.orig_h', 'id.resp_h']

bro_df = df[features]

G = nx.DiGraph()
# gvd = pgv.AGraph(directed=True)
for idex, row in bro_df.iterrows():
    G.add_edge(row['id.orig_h'], row['id.resp_h'])

DG = nx.DiGraph()
name1 = ''
name2 = ''
for index, row in bro_df.iterrows():
    G.add_edge(row[0], row[0])

pos = graphviz_layout(G, prog='dot')
nx.draw(G, pos, with_labels=False)
plt.savefig('directed_networkx_graph.png')

plt.gcf().clear()

pr = nx.pagerank(G)
plt.hist(pr.values())
plt.title("PageRank Values of HTTP Connections")
plt.xlabel("PageRank Value")
plt.savefig("pagerank.png")
# print(pr)

plt.gcf().clear()
ax = bro_df['id.orig_h'].resample('1S').count().plot()