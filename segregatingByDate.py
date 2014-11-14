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
    for line in data_file:
        record = json.loads(line)
        date = record[5]
        if (date in dataByDate.keys()):
            if (record[4] not in dataByDate[date]['recordIDs']):
                dataByDate[date]['records'].append(record)
                dataByDate[date]['recordIDs'].append(record[4])
                dataByDate[date]['count'] += 1
        else:
            dataByDate[date] = { 'records': [record], 'count': 1, 'recordIDs': [record[4]]}
    return dataByDate
    
if __name__== '__main__':
    output = main()
    print json.dumps(output)
