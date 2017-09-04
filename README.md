# Sherlock

## INTRODUCTION

Sherlock is an open-source forensic tookit for analyzing the
relationships among digital evidence. Sherlock enables
investigators to identify, correlate and reason about evidence.

## OVERVIEW

Sherlock allows one to analyze the relationships among evidence.
These relationships may present themselves in various ways. For
example: PPID -> PID, PID -> Socket, Parent INode -> Child INode.
The explorations of these relationships through graph theory,
link analysis, and probabilistic graphical models allows for a
sound analysis of the evidence.

## METHODOLOGY

![alt text](https://github.com/inp2/sherlock/blob/master/pics/Scientific%20Method.png)

### Observe Evidence

In order to observe evidence we rely on data mining, graph theory, and link analysis.

#### Hyperlink-Induced Topic Search (HITS)

In order to determine which pieces of evidence are important to other pieces of evidence. We believe that in determining these pieces will allow inferring the high-level actions taken by the user. The hub value estimates the value by the links to other nodes.

#### PageRank

PageRank is a link analysis algorithm that computes the ranking of nodes in the graph based on the structure of incoming edges. THe PageRank value will identify key pieces of evidence.

#### Data Mining

### Formulate Hypothesis

The ability to draw conclusive assessment about a case, an examiner to find significant tests to evaluate the simplest hypotheses. Denote a mapping between evidence set E, and hypothesis H.

#### Graph Traversal

Graph traversal is the process of visiting each node in a graph.

### Evaluate Hypotheses

### Report Results

## REQUIREMENTS

## INSTALL

## EXAMPLES

## REFERENCES
