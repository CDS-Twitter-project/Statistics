# -*- coding: utf-8 -*-
#   Segregating tweet-data by date.
#   Author - Janu Verma
#   jv367@cornell.edu

import json
import sys
import urllib2




def main():
    data_file = open(sys.argv[1])
    dataByDate = {}
    tweets = []
    for line in data_file:
        record = json.loads(line)
        date = record[5]
        if (record[1] not in tweets):
            tweets.append(record[1])
            if (date in dataByDate.keys()):
                dataByDate[date]['records'].append(record)
                dataByDate[date]['count'] += 1
            else:
                dataByDate[date] = { 'records': [record], 'count': 1}
    return dataByDate
    
if __name__== '__main__':
    output = main()
    print json.dumps(output)
