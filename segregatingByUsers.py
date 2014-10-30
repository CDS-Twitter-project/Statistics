# -*- coding: utf-8 -*-
#	Segregating tweet-data by users.
#	Author - Janu Verma
#	jv367@cornell.edu

import json
import sys
import urllib2




def main():
	data_file = open(sys.argv[1])
	dataByUser = {}
	for line in data_file:
		record = json.loads(line)
		user = record[0]
		if (user in dataByUser.keys()):
			dataByUser[user].append(record)
		else:
			dataByUser[user] = [record]
	return dataByUser
	
if __name__== '__main__':
	print main()			