# -*- coding: utf-8 -*-
#	Extracting relevant information from the json tweet.
#	Author - Janu Verma
#	jv367@cornell.edu

import json
import sys
import urllib2


input = open(sys.argv[1])


duplicates = set()
for line in input:
    data = json.loads(line)
    text = data["text"].encode('utf-8')
    fav_count = data["favorite_count"]
    retweets = data["retweet_count"]
    index = data["id"]
    date = data["created_at"]
    date = date[:10]
    user_id = data["user"]["id"]
    try:
    	hashtags = data["entities"]["hashtags"]
    except:
    	hashtags = "No Hashtags."	
    record = json.dumps([user_id, text, fav_count, retweets, index, date, hashtags])
    if not(index in duplicates):
    	duplicates.add(index)
    	print record