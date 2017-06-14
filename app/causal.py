#!/usr/bin/env python2.7

import os
import subprocess
import networkx as nx
import operator
import sys
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import write_dot
from networkx.drawing.nx_agraph import graphviz_layout
import pygraphviz as pgv
from collections import Counter
import numpy as np

# Parse information from file
# Create graph
def observe_evidence(filename):
    glst = []
    fname = str("uploads/" + filename)
    with open(fname) as fh:
        for line in fh:
            ln = line.strip()
            evt = ln.split("->")
            if len(evt) > 1:
                d = {"Parent": evt[0].strip(" "), "Child":evt[1].strip(" ")}
                glst.append(d)

    # Build graphs
    dg = nx.DiGraph()
    gvd = pgv.AGraph(directed=True)
    for node in glst:
        dg.add_node(node['Child'])
        gvd.add_node(node['Child'])
        dg.add_node(node['Parent'])
        gvd.add_node(node['Parent'])
        dg.add_edge(node['Parent'], node['Child'])
        gvd.add_edge(node['Parent'], node['Child'])

    # Create folder for this case
    # FOLDER_NAME = filename.split(".")[0].encode("utf-8")
    # subprocess.call(['mkdir', FOLDER_NAME])
    pos = nx.spring_layout(dg)
    nx.draw(dg,pos)
    plt.savefig(filename + ".png", format="PNG")
    
    ''' # Run graph analysis
    # PageRank
    pr = nx.pagerank(dg)
    pr = sorted(pr.items(), key=operator.itemgetter(1), reverse=True)
    # HITS
    h,a = nx.hits(dg)
    h = sorted(h.items(), key=operator.itemgetter(1), reverse=True)'''

def summary(graph):
    degr = []
    x = []
    y = []
    # Get the degree of each node
    for node in graph:
        # print node
        degr.append(graph.degree(node))
        # print node + " " + str(graph.degree(node))
    # Get the number of nodes in a graph
    n = nx.number_of_nodes(graph)
    dis_deg = Counter(degr)
    print dis_deg
    x = []
    for key, value in Counter(degr).iteritems():
        y.append(key)
        x.append((float(value)/float(n)))
    num_bins = 50
    counts, bins = np.histogram(x, bins=num_bins)
    bins = bins[:-1] + (bins[1] - bins[0])/2
    probs = counts/float(counts.sum())
    # print probs.sum()
    # Probability Mass Function
    plt.bar(bins, probs, 1/num_bins)
    # plt.show()
    print y
    print x
    

    # Check for Paths Between Two Nodes
    with open("ShortestPath.txt", "wb") as fh:
        for node in graph:
            fh.write(str(node) + " " + str(nx.single_source_shortest_path(graph,node)))    
