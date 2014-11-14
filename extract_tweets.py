import sys
import json

if __name__ == '__main__':
    s = set()
    data_file = open(sys.argv[1])
    for row in data_file:
       tweet = json.loads(row)
       s.add(tweet[1].encode('utf-8'))
    for t in s:
        print t
