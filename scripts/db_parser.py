#!/usr/bin/python
import sqlite3
import sys
import pandas as pd

cnx = sqlite3.connect(sys.argv[1])

df = pd.read_sql("SELECT * FROM *", cnx)

print(df.columns)
