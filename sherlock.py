#!/usr/bin/env python2.7
from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from StringIO import StringIO
import csv
import os
import networkx as nx
import operator
import sys
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import write_dot
from networkx.drawing.nx_agraph import graphviz_layout
import pydot
import pygraphviz as pgv
from collections import Counter
import numpy as np
from scipy import stats
from scipy.stats import norm

# Build a list from the data in the file
# Input: File
# Output: PNG, DOT file of graphs
def graph_builder(filename):
    # Create a list from uploaded file
    graph_list = parse_file(filename)
    # Build a directed graph
    graph = directed(graph_list)
    # Create undirected graph and AGraph
    g, G = build_graph(graph_list)
    summary(g)
    G.layout(prog='fdp')
    G.draw('test.png')
    G = pgv.AGraph(g)
    g.write("file.dot")
    
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
    
    with open("graph_view.csv", "wb") as fh:
        # Write header row
        writer=csv.writer(fh)
        writer.writerow(["NodeID", "PageRank","Hub", "KatzCentrality", "DegreeCentrality"])
        # Calculate values of graph
        pr = nx.pagerank(graph)
        hits,au = nx.hits(graph)
        adc = nx.katz_centrality(graph)
        sorted_x = sorted(adc.items(), key=operator.itemgetter(1))
        # print sorted_x
        dc = nx.degree_centrality(graph)
        for (k1,v1), (k2,v2), (k3,v3), (k4,v4) in zip(pr.items(), hits.items(), adc.items(), dc.items()):
            writer.writerow([k1,v1,v2,v3,v4])

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
# Output: PDF Directed Graph, Undirected Graph, PageRank, HITs
#         Directed Graph Visualization, Data Mining Results
def observe(filename):
    # Create Observe PDF
    pdf = canvas.Canvas("observe.pdf")
    
    # Parse the file
    glst = parser(filename)

    # Build graph
    g, G = builder(glst)

    # Visualize Graph
    G.layout(prog='fdp')
    G.draw("observe.png")
    pdf.drawImage("observe.png", 0, 0, 10, 10)
    pdf.showPage()
    pdf.save()
    
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
