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

    gvd.layout(prog='neato')
    gvd.draw('static/' + filename + '.png')
    
    # Run graph analysis
    # PageRank
    pr = nx.pagerank(dg)
    pr = sorted(pr.items(), key=operator.itemgetter(1), reverse=True)
    
    # HITS
    h,a = nx.hits(dg)
    h = sorted(h.items(), key=operator.itemgetter(1), reverse=True)

    # Katz Centrality
    katz = nx.katz_centrality(dg)
    katz = sorted(katz.items(), key=operator.itemgetter(1), reverse=True)

    # Degree Centrality
    dcent = nx.degree_centrality(dg)
    dcent = sorted(dcent.items(), key=operator.itemgetter(1), reverse=True)
    
    # Return and put in a table
    return h, pr, katz, dcent, dg

def formulate_evidence(src, trg, dg):
    paths = nx.all_simple_paths(dg, src, trg)
    return paths

def evaluate_evidence(dg, paths):
    degr = []
    x = []
    y = []
    deg_dis = []
    # Get the degree of each node
    for node in dg:
        degr.append(dg.degree(node))
    # Get the number of nodes in a graph
    n = nx.number_of_nodes(dg)
    dis_deg = Counter(degr)
    for key, value in Counter(degr).iteritems():
        y.append(key)
        v = (float(value)/float(n))
        x.append((float(value)/float(n)))
        dict = {'Count': key, 'Degree': v}
        deg_dis.append(dict)
    return deg_dis
