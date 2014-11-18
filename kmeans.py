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
for line in input_file:
	record = json.loads(line)
	tweet = record[1]
	allTweets.append(tweet)


vectorizer = CountVectorizer(min_df=0, stop_words='english')
X = vectorizer.fit_transform(allTweets)
X = X.toarray()

kmeans = KMeans(n_clusters=5)
clusters = kmeans.fit_predict(X)

print clusters

