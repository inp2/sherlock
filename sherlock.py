#!/usr/bin/env python2.7
from networkx.drawing.nx_pydot import write_dot
from networkx.drawing.nx_agraph import graphviz_layout
from collections import Counter
from scipy import stats
from scipy.stats import norm
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from matplotlib import rcParams
from sklearn import cluster

import csv
import os
import operator
import sys
import pydot
import sklearn

import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns
    
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
    # print dis_deg
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
    # print y
    # print x
    
# Input: List of Dictionaries
# Output: Two Directed Graphs
def builder(glst):
    dg = nx.DiGraph()
    gvd = pgv.AGraph(directed=True)
    for node in glst:
        dg.add_node(node['Child'])
        gvd.add_node(node['Child'])
        dg.add_node(node['Parent'])
        gvd.add_node(node['Parent'])
        dg.add_edge(node['Parent'], node['Child'])
        gvd.add_edge(node['Parent'], node['Child'])
    return dg, gvd

# Input: file
# Output: PDF File - Directed Graph Visualization
#         CSV File - Table of PageRank, HITs,
#         Degree Centrality, Katz Centrality
#         TXT File - Data Mining Results
# Location: case
def observe(filename):
    # Make a folder
    os.makedirs("case")
    
    # Parse the file
    glst = parser(filename)

    # Build graph
    g, G = builder(glst)

    # Visualize Graph
    G.layout(prog='fdp')
    G.draw("case/observe.pdf")
    
    # Determine HITs, PageRank, Katz Centrality, Degree Centrality
    with open("case/observe.csv", "wb") as fh:
        # Write header row
        writer=csv.writer(fh)
        writer.writerow(["NodeID", "PageRank","Hub", "KatzCentrality", "DegreeCentrality"])
        # Calculate values of graph
        pr = nx.pagerank(g)
        hits,au = nx.hits(g)
        adc = nx.katz_centrality(g)
        sorted_x = sorted(adc.items(), key=operator.itemgetter(1))
        dc = nx.degree_centrality(g)
        for (k1,v1), (k2,v2), (k3,v3), (k4,v4) in zip(pr.items(), hits.items(), adc.items(), dc.items()):
            writer.writerow([k1,v1,v2,v3,v4])

    # Observe with Data Mining
    df = pd.read_csv('case/observe.csv')
    df.describe().to_csv("case/observe.txt")

    df.columns = ['PageRank', 'Hub']
    # plt.scatter(df.PageRank, df.hub)
    # plt.xlabel('PageRank')
    # plt.ylabel('Hub')
        
# Parse the file
# Input: file
# Output: A list of dictionaries
def parser(filename):
    grph = []
    with open(filename) as f:
        lines = f.readlines()[1:]
        for line in lines:
            line = line.strip()
            evt = line.split("->")
            if len(evt) > 1:
                dict = {"Parent": evt[0].strip(" "), "Child":evt[1].strip(" ")}
                grph.append(dict)
    return grph

# Build a directed graph
# Input: List of Directories
# Output: Directed GRaph
def directed(graph_list):
    lst = []
    dg = nx.DiGraph()
    # Replace PID with PName
    for item in graph_list:
        dg.add_node(item['Parent'])
        dg.add_node(item['Child'])
        dg.add_edge(item['Parent'], item['Child'])
    return dg

if __name__ == "__main__":
    sciMthd=True
    while sciMthd:
        print("""
        1. Observe Evidence
        2. Formulate Hypotheses
        3. Evaluate Hypotheses
        4. Report Results
        5. Exit
        """)
        sciMthd=raw_input("Choose a Phase: ")
        if sciMthd == "1":
            filename = raw_input("\nEnter Filename: ")
            observe(filename)
            # Run Program
            # Write results to a PDF
            # Print out location of PDF
        elif sciMthd == "2":
            src = raw_input("\nEnter Source Node of your Hypothesis: ")
            # Run graph traversal, print to screen
        elif sciMthd == "3":
            src = raw_input("\nEnter Path of your Hypothesis: ")
            # Run ProbLog, Print to screen
        elif sciMthd == "4":
            "Print Results"
        elif sciMthd == "5":
            print "\nExit"
            break
        else:
            print "\nUnknown Option Selected!"
