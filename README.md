# Sherlock: A Digital Forensic Analysis Toolkit

### Authors

[Imani Palmer] (imanipalmer.com)

Benjamin Pollack

Young Li

## INTRODUCTION

![The Digital Forensic Investigative Process](http://4.bp.blogspot.com/_Jgk3LbZWY8I/TL4_gGa186I/AAAAAAAAAIU/P4V8Y9lbZFo/s1600/nist+process.jpg "The Digital Forensic Investigative Process")

The analysis phase of the digital forensic process is very
complex. This phase grows more complicated as the size and
ubiquity of digital devices increase. There are many tools
aimed at assisting the investigaor in the analysis problem;
however, they do not address growing challenges. Sherlock 
is an open-source forensic tookit for analyzing the
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
2. Formulate Hypotheses
3. Evaluate Hypotheses
4. Exit

Choose a Phase: ```1```

``` Enter 1 into the prompt```

Output:

Enter Filename: ```example.txt```

``` Enter example.txt into the prompt, Need to give the full path information for this prompt```

Output:

```[1. 3. 4]```
```[0.666666. 0.222222. 0.111111]````
```This information is important for the determination of likelihood of a hypothesis```

1. Observe Evidence
2. Formulate Hypotheses
3. Evaluate Hypotheses
4. Exit

Choose a Phase: ```2```

```Enter 2 into the prompt```

Output:

Enter Source Node of your Hypothesis: ```explorer.exe```

```Enter explorer.exe into the prompt```

Output:

[('explorer.exe', 'AcroRd32.exe'), ('AcroRd32.exe', 'notepad.exe'), ('AcroRd32.exe', '192.168.1.115')]
[('explorer.exe', 'firefox.exe'), ('firefox.exe', 'Dropbox'), ('firefox.exe', '54.201.155.11'), ('firefox.exe', '23.209.190.51')]

This is a link of paths in the graph, for example (explorer.exe - AcroRd32.exe - notepad.exe), means GUI opened a PDF document and opened notepad application.

1. Observe Evidence
2. Formulate Hypotheses
3. Evaluate Hypotheses
4. Exit

Choose a Phase: ```3```

```Enter 3 into the prompt```

Enter Source Node of your Hypothesis: ```explorer.exe```

Enter Target Node of your Hypothesis: ```192.168.1.115```

explorer.exe 0.2222222
AcroRd32.exe 0.2222222
192.168.1.115 0.6666667

This are the likelihoods for each individual piece of evidence.

1. Observe Evidence
2. Formulate Hypotheses
3. Evaluate Hypotheses
4. Exit

Choose a Phase: ```4```

Done!

## Documentation

Documentation and additional information is available:

[Exploring Digital Evidence with Graph Theory](https://commons.erau.edu/cgi/viewcontent.cgi?article=1374&context=adfsl) <br />
[Towards Sound Analysis of Computer Evidence](https://www.nist.gov/sites/default/files/documents/2017/08/23/imanipalmerwednesdayafternoonsession.pdf) <br />
