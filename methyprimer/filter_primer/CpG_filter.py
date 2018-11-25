import os 
import re

def CpG_filter(p3outfile):
	
	file = open(p3outfile)
	for line in file:
		line = line.strip()
		if line.startswith("SEQUENCE_ID"):
			SEQUENCE_ID,locs = line.split("=")
			primer = dict()
		if re.search('_SEQUENCE',line):
