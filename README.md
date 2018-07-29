# sherlock: a digital forensic analysis toolkit

## Overview

The analysis phase of the digital forensic investigative process is very complex.
This phase grows more complicated as the size and ubquity of digital devices increases.
There are many tools aimed at assisting the investigator in the extraction of digital
evidence; however, very few aimed at analyzing the evidence. sherlock is an open-source
forensic toolkit for analyzing digital evidence. sherlock enables investigators to
identify, correlate and reason about evidence.

## Installation

Requires Python 3.0

### Ubuntu Installation

```apt install python3 ```

```apt install python-pip ```

```pip install -r requirements.txt ```

### Mac Installation

Comming Soon

### Windows Installation

Comming Soon

### Virtualization of Application

Comming Soon

### Web Application

Comming Soon

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

```[1. 3. 4]```
```[0.666666. 0.222222. 0.111111]````
```This information is important for the determination of likelihood of a hypot\
hesis. There is more information in the folder data```

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

[('explorer.exe', 'AcroRd32.exe'), ('AcroRd32.exe', 'notepad.exe'), ('AcroRd32.\
exe', '192.168.1.115')]
[('explorer.exe', 'firefox.exe'), ('firefox.exe', 'Dropbox'), ('firefox.exe', '\
54.201.155.11'), ('firefox.exe', '23.209.190.51')]

This is a link of paths in the graph, for example (explorer.exe - AcroRd32.exe \
- notepad.exe), means GUI opened a PDF document and opened notepad application.

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

[Exploring Digital Evidence with Graph Theory](https://commons.erau.edu/cgi/vie\
wcontent.cgi?article=1374&context=adfsl) <br />
[Towards Sound Analysis of Computer Evidence](https://www.nist.gov/sites/defaul\
t/files/documents/2017/08/23/imanipalmerwednesdayafternoonsession.pdf) <br />

## Contributors

### Researchers

[Imani Palmer](https://imanipalmer.com) & [Young Li](https://usipeus.github.io/)

### Developers

[Sarah Moulton](https://github.com/suspiciousCloud) & [Benjamin Pollak](https://github.com/BenjaminPollak)
