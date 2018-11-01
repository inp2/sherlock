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
    try: 
        name1 = socket.gethostbyaddr(str(row['id.orig_h']))
    except:
        G.add_node(row['id.orig_h'])
    try:
        name2 = socket.gethostbyaddr(str(row['id.resp_h']))
    except:
        G.add_node(row['id.resp_h'])
    if name1 and name2:
        G.add_edge(name1[0], name2[0])
    elif name1:
        G.add_edge(name1[0], row['id.resp_h'])
    elif name2:
        G.add_edge(row['id.orig_h'], name2[0])

# pos = graphviz_layout(G, prog='dot')
# nx.draw(G, pos, with_labels=True, node_size=100, node_color='w')
# plt.savefig('directed_networkx_graph.png')
write_dot(G, "test1.dot")
write_dot(DG, "test2.dot")
