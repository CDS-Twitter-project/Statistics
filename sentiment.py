import csv
import json
import sys
import re


## Open AFINN File and Create a Dictionary of Terms and Sentiment Scores 
afinn_file = open(sys.argv[1])
scores = {}                             # initialize an empty dictionary
for line in afinn_file:
    term, score  = line.split("\t")     # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)           # Convert the score to an integer



## Define Sentiment of a Text - Line
def sentiment(line):
	score = 0
	words = re.findall(r"\b[a-z]+\b", line, re.I)
	#words = line.split()
	for w in words:
		if (w in scores):
			score = score + scores[w]       
	return score


##	Open the input tweet file. 
## Each line is of the form [user_id, tweet_text, fav_count, retweets, index, date, hashtags]
#input_file = open(sys.argv[2])
#for line in input_file:
#	record = json.loads(line)
#	tweet_text = record[1]
#	sentiment_score = sentiment(tweet_text)
#	print sentiment_score
	
	
input_file = open(sys.argv[2])
with open("sentiment_by_tweet.csv", 'wb') as csvfile:
	writer = csv.writer(csvfile)
	i = 0
	for line in input_file:
		sentiment_score = sentiment(line)
		writer.writerow([i, sentiment_score])
		i += 1
	

#for line in input_file:
#	mainDict = json.loads(line)
#	for date in mainDict.keys():
#		records = mainDict[date]['records']
#		numberOfTweets = mainDict[date]['count']
#		totalSentiment = 0.0
#		for x in records:
#			tweetText = x[1]
#			score = sentiment(tweetText)
#			totalSentiment += score
#		print "%s, %f" % (date, (totalSentiment / numberOfTweets))
