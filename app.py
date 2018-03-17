from flask import Flask, render_template

import networkx as nx

from NetworkxD3 import simpleNetworkx

app = Flask(__name__)

@app.route('/')
def webprint():
    observe('example.txt')
    return render_template('Net.html')

def observe(filename):
    graph_list = parser(filename)
    directed_graph = builder(graph_list)
    simpleNetworkx(directed_graph)

def builder(graph_list):
    dg= nx.DiGraph()
    for node in graph_list:
        dg.add_edge(node['Parent'], node['Child'])
    return dg
    
def parser(filename):
    graph_list = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            evt = line.split(",")
            dict = {"Parent": evt[0].strip(" "), "Child": evt[1].strip(" ")}
        graph_list.append(dict)
    return graph_list
        
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
