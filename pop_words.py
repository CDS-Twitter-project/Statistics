import json
import sys
import operator
import re
from collections import *

### Common_words needs to be changed. 
common_words = ["https", "four","anne", "miss", "all", "their", "today", "rt" "very", "don", "what", "minute", "amp", "saying", "full", "it", "june", "year", "makes", "gets", "xckawitkip", "rather", "now", "not", "side", "want","read","list", "done", "less",  "kswofqwgsr", "m","is","up", "class", "nothing", "but", "kwerb", "important", "did", "nice", "which", "when","who", "how", "wonder", "other", "k", "need", "say", "rimalovski", "inc", "an", "int", "v", "below", "those", "wkqvhcdsex", "inside", "kind", "low", "koller", "first", "or", "hvdcsmzpte", "wlqejuci", "qzeykygwko", "teach", "put", "become", "lasts", "cause", "may", "our", "nbieymksdu", "found", "everyone", "page", "vbin", "know", "five", "break", "matters",  "at", "in","s", "on", "this", "that", "most", "here", "there", "via", "do", "re", "by", "be", "d", "as", "than", "its", "will", "shall", "into", "one", "w","for", "of", "http", "a", "with", "you", "your", "yours", "i", "me", "my", "mine", "yours", "about", "off", "get", "would", "should", "rt", "we", "out", "us","for", "am", "are", "was","were", "have", "has", "had", "to", "from", "his", "him", "her", "just", "the", "co", "t", "across", "2012"]
input = open(sys.argv[1])

def main(n):
    freq_dict = defaultdict(int)
    for line in input:
        data = json.loads(line)
        tweet = data["text"].encode('utf-8')
        words = re.findall(r"\b[a-z]+\b",tweet,re.I)
        words = [w.lower() for w in words]
        for word in words:
            if not(word in common_words):
                freq_dict[word] += 1

    sorted_wordcount = sorted(freq_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_wordcount[:n]            

print main(6)
