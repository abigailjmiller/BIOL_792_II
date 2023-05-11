#! /usr/bin/env python

import re
import sys
import os
import pandas as pd

temp_hood_1 = 0
temp_hood_2 = 0
temp_hood_3 = 0
temp_hood_4 = 0
temp_hood_5 = 0
temp_hood_6 = 0


directory = 'iButton_data_hood' #define the directory
for filename in os.listdir(directory): #for each file in directory, do this
	if filename.endswith('.csv'): #if the file ends in csv open it
		with open(os.path.join(directory, filename)) as f: 
			lines = f.readlines() #skip first lines because they're just diagnostics on ibutton
			for line in lines[15:]: #skip first lines because they're just diagnostics on ibutton
				line = line.strip('\n') #strip the line endings
				line = line.split(',')	#separate each element by comma
				if filename == "Hood_Button_1.csv":
					temp_hood_1 += float(line[2])
					temp_1 = temp_hood_1/731
					with open("New_hood_1.csv", "a") as hood_1:
						print(filename, temp_1, file=hood_1)
						hood_1.close()
				elif filename == "Hood_Button_2.csv":
					temp_hood_2 += float(line[2])
					temp_2 = temp_hood_2/731
					with open("New_hood_2.csv", "a") as hood_2:
						print(filename, temp_2, file=hood_2)
						hood_2.close()
				elif filename == "Hood_Button_3.csv":
					temp_hood_3 += float(line[2])
					temp_3 = temp_hood_3/731
					with open("New_hood_3.csv", "a") as hood_3:
						print(filename, temp_3, file=hood_3)
						hood_3.close()
				elif filename == "Hood_Button_4.csv":
					temp_hood_4 += float(line[2])
					temp_4 = temp_hood_4/731
					with open("New_hood_4.csv", "a") as hood_4:
						print(filename, temp_4, file=hood_4)
						hood_4.close()
				elif filename == "Hood_Button_5.csv":
					temp_hood_5 += float(line[2])
					temp_5 = temp_hood_5/731
					with open("New_hood_5.csv", "a") as hood_5:
						print(filename, temp_5, file=hood_5)
						hood_5.close()
				elif filename == "Hood_Button_6.csv":
					temp_hood_6 += float(line[2])
					temp_6 = temp_hood_6/731
					with open("New_hood_6.csv", "a") as hood_6:
						print(filename, temp_6, file=hood_6)
						hood_6.close()
				else:
					print("no")

					
						
							