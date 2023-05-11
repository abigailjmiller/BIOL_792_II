#! /usr/bin/env python

import re
import sys
import os
import pandas as pd


last_lines = open("last_lines_table.csv", "a")
directory = 'New_table' #define the directory
for filename in os.listdir(directory): #for each file in directory, do this
	if filename.endswith('.csv'): #if the file ends in csv open it
		with open(os.path.join(directory, filename)) as f: 
			df = pd.read_csv(f)
			bottom = df.tail(1)
			print(bottom, file=last_lines)
			