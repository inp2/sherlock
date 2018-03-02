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

In order to observe evidence we rely on data mining, graph theory, 
and link analysis.

## INSTALL

You need Python 2.7

#### Ubuntu
```apt install python-pip python-sklearn ```

```pip install -r requirements.txt```

```apt install python```

## Quick Start

```python sherlock.py```

Output:

1. Observe Evidence
2. Formaulate Hypotheses
3. Evaluate Hypotheses
4. Exit

Choose a Phase: ```1```

``` Enter 1 into the prompt```

## Documentation

Documentation and additional information is available:

![Exploring Digital Evidence with Graph Theory](https://commons.erau.edu/cgi/viewcontent.cgi?article=1374&context=adfsl) <br />
![Towards Sound Analysis of Computer Evidence](https://www.nist.gov/sites/default/files/documents/2017/08/23/imanipalmerwednesdayafternoonsession.pdf) <br />
