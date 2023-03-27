#! /usr/bin/env python

import re
import sys

#read in file
#Bloom = "Bloom_etal_2018_Reduced_Dataset.csv"
#InFile= open(Bloom, 'r')
#skip first line (header)
#next(InFile)

#set totalsize value to 0 to start
#totalsize = 0

#for loop that will go through each line in the file
#for Line in InFile:
	
	#strip line endings
#	Line = Line.strip('\n') 
	#separate each element by comma
#	Line = Line.split(',')
	
	#add each logbodysize to the previous line
#	totalsize += float(Line[1])
	
	#print outputs
#	print(Line[0], Line[3], totalsize)


#create empty dictionary
#fill out dictionary with keys
#turn dictionary into list
#print "big" or "small"

animal_dict = {}
animal_dict['cat']= 25
animal_dict['dog'] = 30
animal_dict['bear']= 35
animal_dict['frog']= 5
	
an_list = list(animal_dict)

for i in an_list:
	if animal_dict[i] > 20:
		print('Big')
	else:
		print('Small')
