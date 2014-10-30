# -*- coding: utf-8 -*-
#	Segregating tweet-data by date.
#	Author - Janu Verma
#	jv367@cornell.edu

import json
import sys
import urllib2




def main():
	data_file = open(sys.argv[1])
	dataByDate = {}
	for line in data_file:
		record = json.loads(line)
		date = record[5]
		if (date in dataByDate.keys()):
			dataByDate[date].append(record)
		else:
			dataByDate[date] = [record]
	return dataByDate
	
if __name__== '__main__':
	print main()				