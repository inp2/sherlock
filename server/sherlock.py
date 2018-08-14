#!/usr/bin/env python2.7

from networkx.drawing.nx_pydot import write_dot
from networkx.drawing.nx_agraph import graphviz_layout
from collections import Counter # builtin
from collections import defaultdict # builtin
from datetime import datetime
import time

import csv # builtin
import os # builtin
import operator # builtin
import sys # builtin
import pydot
import sklearn

import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv
import numpy as np
import pandas as pd

from PAFunc import testworks, parseComm, getTimeStr, getDateTimeUnix


# Input: Source Node, Target Node, Graph
# Output: Confidence Score of Hypothesis
def evaluate(src, trg, grph):
    # Check if path exists
    if nx.has_path(grph, src, trg):
        g = nx.shortest_path(grph, source=src, target=trg)
    else:
        print "path does not exist"

    degr = []
    x = []
    y = []
    # Get the degree of each node
    for node in grph:
        degr.append(grph.degree(node))
    # Get the number of nodes in a graph
    n = nx.number_of_nodes(grph)
    dis_deg = Counter(degr)
    x = []
    for key, value in Counter(degr).iteritems():
        y.append(key)
        x.append((float(value)/float(n)))
    num_bins = 50
    counts, bins = np.histogram(x, bins=num_bins)
    bins = bins[:-1] + (bins[1] - bins[0])/2
    probs = counts/float(counts.sum())

    for item in g:
        dg = grph.degree(item)
        num = y.index(dg)
        print item + " " + str(x[num])
    # Please use problog to determine confidence score

# Input: Source Node
# Output: Edges in depth-first-search
def formulate(src, grph, graph=-1):
    formList=list(nx.dfs_edges(grph, src))
    print formList

    if graph==-1:
        return

    fG = nx.DiGraph()

    for node in formList:
        fG.add_edge(node[0], node[1])

    pos = nx.layout.circular_layout(fG)
    nodes = nx.draw_networkx_nodes(fG, pos, node_size=100, node_color='blue', alpha=.5)
    edges = nx.draw_networkx_edges(fG, pos, node_size=100, arrowstyle='->', arrowsize=10, width=2)

    ax = plt.gca()
    ax.set_axis_off()

    #plt.savefig(caseFile+'/formulate_graph.png')
    #plt.show()


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
        dg.add_edge(node['Parent'], node['Child'], weight=1)
        gvd.add_edge(node['Parent'], node['Child'], weight=1)
    return dg, gvd

# Input: file
# Output: PDF File - Directed Graph Visualization
#         CSV File - Table of PageRank, HITs,
#         Degree Centrality, Katz Centrality
#         TXT File - Data Mining Results
# Location: case
caseFile=""
def observe(filename, colorApart=-1, accessOrder=-1):

    # Make a folder

    global caseFile
    caseFile="case"
    if not os.path.isdir(caseFile):
        os.makedirs(caseFile)
    else:
        i=1
        while(1==1):
            if not os.path.isdir(caseFile+str(i)):
                os.makedirs(caseFile+str(i))
                caseFile=caseFile+str(i)
                break
            i+=1

    # Parse the file
    glst = parser(filename)

    # Build graph
    g, G = builder(glst)

    # Visualize Graph
    #G.layout(prog='fdp')
    #G.draw("case/directed_graph.png")

    #NEW Graph NOTE the old graphs still exist but are not displayed
    sG = nx.DiGraph()

    for node in glst:
        sG.add_edge(node['Parent'], node['Child'], weight=node['Time'])

    #pos = nx.layout.spring_layout(sG)
    #pos = nx.layout.spectral_layout(sG)
    #pos = nx.layout.shell_layout(sG)
    pos = nx.layout.circular_layout(sG)
    nodes = nx.draw_networkx_nodes(sG, pos, node_size=100, node_color='blue', alpha=.5)





    nodeList=sG.nodes()
    #NOTE this is NOT a node dfs it is an EDGE dfs
    dfsList=list(nx.edge_dfs(sG,nodeList))
    accessOrderList = list() #ordered list of nodes by access time
    accessOrderDict = {} #dict of (node, timeInUnix)
    i = 0
    #insert sorted
    #Can you tell I'm a c programmer?
    while i < len(dfsList):
        tNode= dfsList[i]
        nodeTime=getTimeStr(sG[tNode[0]][tNode[1]])
        dtUnix=getDateTimeUnix(nodeTime)

        if i == 0:
            accessOrderList.append(tNode)
            accessOrderDict[tNode]=dtUnix
        elif accessOrderDict[accessOrderList[i-1]]<= dtUnix:
            accessOrderList.append(tNode)
            accessOrderDict[tNode]=dtUnix
        else :
            j=0
            while j < len(accessOrderList):
                if accessOrderDict[accessOrderList[j]] > dtUnix:
                    accessOrderDict[tNode]=dtUnix
                    accessOrderList.insert(j, tNode)
                    break
                j+= 1
        i+= 1

    #print accessOrderList
    if accessOrder != -1:
        for item in accessOrderList:
            print item[1]
            print sG[item[0]][item[1]]

    if colorApart != -1:
        coloredEdges=list();
        regEdges=list();
        i = 0
        while i < len(accessOrderList):
            if i==0:
                regEdges.append(accessOrderList[i])
            elif (getDateTimeUnix(getTimeStr(sG[accessOrderList[i][0]][accessOrderList[i][1]]))- getDateTimeUnix(getTimeStr(sG[accessOrderList[i-1][0]][accessOrderList[i-1][1]])))/60 >= colorApart:
                coloredEdges.append(accessOrderList[i])
            else:
                regEdges.append(accessOrderList[i])

            i+=1

            edge_colors = range(2, len(regEdges) + 2)
            edgesR = nx.draw_networkx_edges(sG, pos, edgelist=regEdges, node_size=100, arrowstyle='->', arrowsize=10, edge_color=edge_colors, width=2)
            edgesC = nx.draw_networkx_edges(sG, pos, edgelist=coloredEdges, node_size=100, arrowstyle='->', arrowsize=10, edge_color='r', width=2)
    else :
        edge_colors = range(2, len(accessOrderList) + 2)
        edges = nx.draw_networkx_edges(sG, pos, node_size=100, arrowstyle='->', arrowsize=10, edge_color=edge_colors, width=2)

    edge_labels = nx.get_edge_attributes(sG,'weight')
    nx.draw_networkx_labels(sG, pos, font_size=10)
    nx.draw_networkx_edge_labels(sG, pos, edge_labels = edge_labels, font_size=5)




    ax = plt.gca()
    ax.set_axis_off()

    plt.savefig(caseFile+'/directed_graph.png')
    #line below for debug
    #plt.show()


    # Determine HITs, PageRank, Katz Centrality, Degree Centrality
    with open(caseFile+"/graph_analysis.csv", "wb") as fh:
        # Write header row
        writer=csv.writer(fh)
        writer.writerow(["NodeID", "PageRank","Hub", "KatzCentrality", "DegreeCentrality"])
        # Calculate values of graph
        pr = nx.pagerank(g)
        degr = []
        x = []
        y = []
        # Get the degree of each node
        for node in g:
            degr.append(g.degree(node))
        # Get the number of nodes in a graph
        n = nx.number_of_nodes(g)
        dis_deg = Counter(degr)
        for key, value in Counter(degr).iteritems():
            y.append(key)
            x.append((float(value)/float(n)))
        print y
        print x
    # Please use problog to determine confidence score
        hits,au = nx.hits(g)
        adc = nx.katz_centrality(g)
        sorted_x = sorted(adc.items(), key=operator.itemgetter(1))
        dc = nx.degree_centrality(g)
        for (k1,v1), (k2,v2), (k3,v3), (k4,v4) in zip(pr.items(), hits.items(), adc.items(), dc.items()):
            writer.writerow([k1,v1,v2,v3,v4])

    # Observe with Data Mining
    df = pd.read_csv(caseFile+ '/graph_analysis.csv')
    df.describe().to_csv(caseFile+"/data_mining.txt")

    df.columns = ['NodeID', 'PageRank', 'Hub', 'KatzCentrality', 'DegreeCentrality']

    fig = plt.figure(figsize=(12,6))
    pr = fig.add_subplot(121)
    hb = fig.add_subplot(122)
    pr.hist(df.PageRank)
    pr.set_title("Histogram of PageRank")
    hb.hist(df.Hub)
    hb.set_title("Histogram of Hubs")
    plt.savefig(caseFile+"/histo_regression_pagerank_hubs.png")

    fig = plt.figure(figsize=(12,6))
    kc = fig.add_subplot(121)
    dc = fig.add_subplot(122)
    kc.hist(df.KatzCentrality)
    kc.set_title("Histogram of Katz Centrality")
    dc.hist(df.DegreeCentrality)
    dc.set_title("Histogram of Degree Centrality")
    plt.savefig(caseFile+"/histo_regression_katzcentrality_degcentrality.png")

    return g

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
            tm = evt[1].split("@")
            if len(evt) > 1:
                dict = {"Parent": evt[0].strip(" "), "Child":tm[0].strip(" "), "Time":tm[1].strip("")}
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

# Input:
# Output:
def initPA():
    print "\n type h for a list of commands"
    print "\n type q or exit to quit personal assistant"
    PAComm=True
    while PAComm:
        PAComm=raw_input("Please state a command: ")
        if PAComm == "h":
            #print("""
            #is [set] in [path/filename]
            #    checks if the set [set] is in the observed evidence in the file [path/filename]
            #""")
            print("""
            1. graph observe [filename]
                shows directed graph of [filename]

            1.1 graph observe [filename] colorApart [minutes]
                shows directed graph of [filename] and colors edges that are [minutes] apart from their previous access time.

            1.2 graph observe [filename] accessOrder
                prints the order in which each element was accessed

            2. graph formulate [source node]
                graphs the link of paths in the graph from [source node]

            """)
        elif PAComm == "q":
            break
        elif PAComm == "exit":
            break
        else:

            id=parseComm(PAComm)
            idComponents = id.split()

            if idComponents[0] == "1":
                grph = observe(idComponents[1])
                fileName=idComponents[1]

            elif idComponents[0] == "1.1":
                grph = observe(idComponents[1], colorApart=int(idComponents[2]))
                fileName=idComponents[1]

            elif idComponents[0] == "1.2":
                grph = observe(idComponents[1], accessOrder=1)
                fileName=idComponents[1]

            elif idComponents[0] == "2":
                if not 'grph' in locals():
                    print "plase observe evidence (step 1) first"
                else:
                   formulate(idComponents[1], grph, graph=1)


            else:
                print "\nCommand Unknown"






if __name__ == "__main__":
    sciMthd=True
    while sciMthd:
        print("""
        1. Observe Evidence
        2. Formulate Hypotheses
        3. Evaluate Hypotheses
        4. Exit
        5. Personal Assistant
        """)
        sciMthd=raw_input("Choose a Phase: ")
        if sciMthd == "1":
            filename = raw_input("\nEnter Filename: ")
            grph = observe(filename)
        elif sciMthd == "2":
            if not 'grph' in globals():
                print "plase observe evidence (step 1) first"
            else:
                src = raw_input("\nEnter Source Node of your Hypothesis: ")
                formulate(src, grph)

        elif sciMthd == "3":
            if not 'grph' in globals():
                print "plase observe evidence (step 1) first"
            else:
                src = raw_input("\nEnter Source Node of your Hypothesis: ")
                trg = raw_input("\nEnter Targe Node of your Hypothesis:\n")
                evaluate(src, trg, grph)

        elif sciMthd == "4" or sciMthd=="q":
            print "\nExit"
            break
        elif sciMthd == "5":
            print "\nPersonal Assistant Selected"
            initPA()
        else:
            print "\nUnknown Option Selected!"
