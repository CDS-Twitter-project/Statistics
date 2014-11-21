# -*- coding: utf-8 -*-
#	Clustering of tweets.
#	Author - Janu Verma
#	jv367@cornell.edu


import numpy as np 
import json
import sys
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.cluster import KMeans



allTweets = []
input_file = open(sys.argv[1])
i = 0
for line in input_file:
	i += 1
	if (i % 20 != 0):
		continue 
	record = json.loads(line)
	tweet = record[1]
	allTweets.append(tweet.encode('utf-8', errors='ignore'))


vectorizer = CountVectorizer(min_df=0, stop_words='english')
X = vectorizer.fit_transform(allTweets)
X = X.toarray()

kmeans = KMeans(n_clusters=int(sys.argv[2]))
clusters = kmeans.fit_predict(X)

clusteredTweets = {i:[] for i in range(5)}
for x,index in zip(allTweets,clusters):
	print x + "\t" + str(index)
	#if (index in clusteredTweets.keys()):
	#	clusteredTweets[index].append(x)
		
#print clusteredTweets

