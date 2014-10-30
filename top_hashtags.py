# -*- coding: utf-8 -*-
#   computing top hashtags in a tweets file.
#   Author - Janu Verma
#   jv367@cornell.edu


import sys
import json
import codecs
import operator

def main():
    tweet_file = open(sys.argv[1])
    hashtags = []
    for line in tweet_file:
        response = json.loads(line)
        if ('entities' in response):
            a = response["entities"]
            b = a["hashtags"]
            if (len(b) > 0):
                for i in range(len(b)):
                    hashtags.append(b[i]['text'].lower())

    freq = {i:hashtags.count(i) for i in set(hashtags)}
    sorted_freq = sorted(freq.iteritems(), key=operator.itemgetter(1))

    i = len(sorted_freq)-1
    while (i >= len(sorted_freq)-50):
        u, v = sorted_freq[i]
        i = i - 1
        print u, v
        
       
          
if __name__ == '__main__':
    main()
