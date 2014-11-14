import sys
import json

if __name__ == '__main__':
    data_file = open(sys.argv[1])
    for row in data_file:
       tweet = json.loads(row)
       print tweet[1]
