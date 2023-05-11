#! /usr/bin/env python

import re
import sys
import os
import pandas as pd

temp_tab_1 = 0
temp_tab_2 = 0
temp_tab_3 = 0
temp_tab_4 = 0
temp_tab_5 = 0
temp_tab_6 = 0


directory = 'iButton_data_table' #define the directory
for filename in os.listdir(directory): #for each file in directory, do this
	if filename.endswith('.csv'): #if the file ends in csv open it
		with open(os.path.join(directory, filename)) as f: 
			lines = f.readlines() #skip first lines because they're just diagnostics on ibutton
			for line in lines[15:]: #skip first lines because they're just diagnostics on ibutton
				line = line.strip('\n') #strip the line endings
				line = line.split(',')	#separate each element by comma
				if filename == "Table_Button_1.csv":
					temp_tab_1 += float(line[2])
					temp_1 = temp_tab_1/731
					with open("New_Table_1.csv", "a") as table_1:
						print(filename, temp_1, file=table_1)
						table_1.close()
				elif filename == "Table_Button_2.csv":
					temp_tab_2 += float(line[2])
					temp_2 = temp_tab_2/731
					with open("New_Table_2.csv", "a") as table_2:
						print(filename, temp_2, file=table_2)
						table_2.close()
				elif filename == "Table_Button_3.csv":
					temp_tab_3 += float(line[2])
					temp_3 = temp_tab_3/731
					with open("New_Table_3.csv", "a") as table_3:
						print(filename, temp_3, file=table_3)
						table_3.close()
				elif filename == "Table_Button_4.csv":
					temp_tab_4 += float(line[2])
					temp_4 = temp_tab_4/731
					with open("New_Table_4.csv", "a") as table_4:
						print(filename, temp_4, file=table_4)
						table_4.close()
				elif filename == "Table_Button_5.csv":
					temp_tab_5 += float(line[2])
					temp_5 = temp_tab_5/731
					with open("New_Table_5.csv", "a") as table_5:
						print(filename, temp_5, file=table_5)
						table_5.close()
				elif filename == "Table_Button_6.csv":
					temp_tab_6 += float(line[2])
					temp_6 = temp_tab_6/731
					with open("New_Table_6.csv", "a") as table_6:
						print(filename, temp_6, file=table_6)
						table_6.close()
				else:
					print("no")

					