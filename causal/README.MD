# hoja

## Introduction

The digital forensic process is burdened by the absence of a standardized methodology for analyzing digital evidence. In this paper, we further the research of digital forensic analysis with evidentiary analytics. Evidentiary analytics is the process of reasoning about digital evidence in order to provide a logical view. We rely on key elements of graph theory to identify important events and the relationships between these events. To this end, we present a prototype hoja. hoja (pronounced o-ha) is an open-source forensic tool for aiding in evidentiary analytics with graph theory. hoja enables investigators to identify key evidence from memory images.

## Requirements

* NetworkX
* Python2.7

## Evidence File Examples

![Input File Example](https://github.com/uiuc-srg/hoja/blob/master/InputFileExample.png)
  
## Usage

`python hoja.py <evidence_file>`

## Dockerize App

We have Dockerize our application in hopes to increase its portability.

### Docker Build Instructions

`cd hoja`

`sudo docker build -t <name> .`

### Docker Run Instructions

`sudo docker run -i -t <name>`

## Author

Imani Palmer is a PhD student at the University of Illinois at Urbana-Champaign conducting research in evidentiary analytics.

## License
[GNU GENERAL PUBLIC LICENSE](https://github.com/uiuc-srg/hoja/blob/master/LICENSE)
