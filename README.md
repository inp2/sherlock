# sherlock: a digital forensic analysis toolkit

## Overview

The analysis phase of the digital forensic investigative process is very complex.
This phase grows more complicated as the size and ubquity of digital devices increases.
There are many tools aimed at assisting the investigator in the extraction of digital
evidence; however, very few aimed at analyzing the evidence. sherlock is an open-source
forensic toolkit for analyzing digital evidence. sherlock enables investigators to
identify, correlate and reason about evidence.

## Installation

Requires Python 2.7.14 or above

### Ubuntu Installation

```apt install python3 ```

```apt install python-pip ```

```pip install -r requirements.txt ```

### Mac OS X Installation

Install python 2 using the Homebrew package manager (https://brew.sh):
 ```brew install python2```

 Verify that the python2 alias is the same as the version installed with Homebrew:
 ```Python2 —version```
 If not, link them:
 ```brew unlink python2 && brew link python2```

 Optionally, point the python alias to python2. This method can also be used to easily switch between python 2 and 3 https://stackoverflow.com/a/43354441

Install Graphviz:
```Brew install Graphviz```

Install Pygraphviz:
```pip install pygraphviz --install-option="--include-path=/usr/local/include/graphviz/" --install-option="--library-path=/usr/local/lib/graphviz"```

Install pkg-config:
```pip install pkg-config```

Navigate to sherlock/server and install requirements:
```pip install -r requirements.txt```


### Windows Installation

Download and install python 2.7.14 from https://www.python.org/downloads/release/python-2714/

Follow these instructions to add it to your path and verify installation:
https://edu.google.com/openonline/course-builder/docs/1.10/set-up-course-builder/check-for-python.html

Follow these instructions to add pip:
https://dev.to/el_joft/installing-pip-on-windows

Download and install the Microsoft Visual C++ Compiler for Python 2.7 from
https://www.microsoft.com/en-us/download/details.aspx?id=44266

In a command prompt window, run:
```pip install scipy ```
```pip install scikit-learn```

Follow the steps here: https://stackoverflow.com/a/44009261 with the following modifications:
for step 2: the file you want is pygraphviz‑1.3.1‑cp27‑none‑win32.whl unless you have an amd processor: pygraphviz‑1.3.1‑cp27‑none‑win_amd64.whl
for step 4: run the command ```pip install pygraphviz-1.3.1-cp27-none-win.whl``` if you do not have an amd processor

Navigate to sherlock/server and install requirements:
```pip install -r requirements.txt```


### Virtualization of Application
Coming Soon

Coming Soon

### Web Application

Coming Soon
=======

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

```Enter example.txt into the prompt, Need to give the full path information for this prompt```

Output:

```[1, 3, 4]```
```[0.666666. 0.222222. 0.111111]```
```This information is important for the determination of likelihood of a hypothesis. There is more information in the folder data```

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

## Literature

Review on the techniques used by this tool:

[Exploring Digital Evidence with Graph Theory](https://commons.erau.edu/cgi/viewcontent.cgi?article=1374&context=adfsl) <br />
[Towards Sound Analysis of Computer Evidence](https://www.nist.gov/sites/default/files/documents/2017/08/23/imanipalmerwednesdayafternoonsession.pdf) <br />

## Contributors

### Researchers

[Imani Palmer](https://imanipalmer.com) & [Young Li](https://usipeus.github.io/)

### Developers

[Sarah Moulton](https://github.com/suspiciousCloud) & [Benjamin Pollak](https://github.com/BenjaminPollak)
