# -*- coding: utf-8 -*-

# 	A graphical representation of a text document. 
# 	Author - Janu Verma
# 	jv367@cornell.edu
# 	@januverma


from __future__ import division
import sys
from collections import *
import operator
from math import *
import networkx as nx 

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
stopwords = set(stopwords)



class TextGraph:
	"""
	Graphical representation of sentences in a text file. 
	Sentences are the nodes and vertices are defined between sentences. 
	"""
	def __init__(self, input_file):
		self.sentences = []
		for line in input_file:
			#line = line.replace("\n", '.')
			#line = line.split('.')
			self.sentences.append(line)


	def wordFrequency(self, sentence):
		"""
		Compute the normalized frequency of occuring of words in the text. 
		"""
		freq_dict = defaultdict(float)
		words = sentence.split()
		words = [x.lower() for x in words]
		words = [x for x in words if len(x) >= 2 and not x.isdigit()]
		for word in words:
			if not(word in stopwords):
				freq_dict[word] += 1
		if len(freq_dict) != 0:
			max_freq = max(freq_dict.iteritems(), key=operator.itemgetter(1))[1]
		for w in freq_dict.keys():
			freq_dict[w] = float(freq_dict[w])
		return freq_dict
		


	def sentenceIntersection(self, s1,s2):
		"""
		Intersection of two sentences 
		"""		
		w1 = self.wordFrequency(s1)
		w2 = self.wordFrequency(s2)
		key1 = w1.keys()
		key2 = w2.keys()
		if (len(key1) == 0) or (len(key2) == 0):
			return 0
		else:
			sum1Sq = sum([pow(w1[x],2) for x in key1]) 
			sum2Sq = sum([pow(w2[x],2) for x in key2]) 	
			commonKeys = set(key1) & set(key2)
			dotProduct = sum([w1[x]*w2[x] for x in commonKeys])
			sim = dotProduct/(sqrt(sum1Sq)*sqrt(sum2Sq))
			return sim
	

	def sentenceGraph(self):
		"""
		Build the graph. 
		"""
		g = nx.Graph()
		for s in self.sentences:
			g.add_node(s)
		for n1 in g.nodes():
			for n2 in g.nodes(): 
				weight = self.sentenceIntersection(n1,n2)
				if (weight > 0.1):
					g.add_edge(n1,n2)
				#g.add_edge(n1,n2, weight=weight)
		return g


	def words(self, d):
		"""
		Compute all the  words in a document. 
		Arguments:
			d : a document
		Returns:
			A list of all the words in the document. 	
		"""
		documents = self.text
		document = documents[d]
		words = document.split()
		words = [x.lower() for x in words]
		words = [x for x in words if not x in stopwords]
		words = [x for x in words if len(x) >= 2 and not x.isdigit()]
		return words		


	def wordDocs(self, d):
		"""
		Arguments:
			d : a document
		Returns:
			A dictionary of all the words in d with d as value. 	
		"""

		docDict = {}
		words = self.words(d)
		words = set(words)
		for w in words:
			docDict[w] = d
		return docDict

	def vocabalury(self):
		"""
		Compute all the unique words in the corpus. 
		Returns:
			A set of all the unique words in the whole corpus of documents. 
		"""
		allDocs = self.text
		allWords = []
		for d in allDocs.keys():
			docWords = self.words(d)
			allWords.extend(docWords)
		allWords = set(allWords)
		return allWords


	def docsContainingWords(self):
		"""
		Compute the documents containg a given word. 
		Returns:
			A dictionary of all the words in the corpus with the value a list
			of all the documents containg the word. 
		"""
		allDocs = self.text
		allWords = self.vocabalury()

		docsContainingWord = {}
		for x in allWords:
			docsContainingWord[x] = []
			for d in allDocs.keys():
				docsForWord = self.wordDocs(d)
				if (x in docsForWord.keys()):
					docsContainingWord[x].append(docsForWord[x])
		return docsContainingWord						


	def keywordGraph(self, cooccuranceThreshold=1):
		"""
		Build the keyword graph. 
		Arguments:
			cooccuranceThreshold : If the cooccurances of two keywords is above
			coocuranceThreshold, there is an edge between the nodes represented
			by the keywords. 
			Default value is 1
		Returns:
			A networkx graph with keywords as nodes and there is an edge between two nodes
			if their similarity value is greater than similarityThreshold.
		"""	
		docsForWords = self.docsContainingWords()
		h = nx.Graph()
		for w in self.vocabalury():
			h.add_node(w)

		for w1 in h.nodes():
			for w2 in h.nodes():
				weight = len(set(docsForWords[w1]) & set(docsForWords[w2]))
				if (weight > cooccuranceThreshold):
					h.add_edge(w1,w2,weight=weight)

		return h			
			






