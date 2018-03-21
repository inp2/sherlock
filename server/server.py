#!/usr/bin/env python2.7

# imports
from flask import Flask
import sherlock as shr

app = Flask(__name__)

@app.route('/')
def observe():
    grph = shr.observe("example.txt")
    if(type(grph) is not None):
        return "exists"
