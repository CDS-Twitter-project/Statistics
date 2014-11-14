# -*- coding: utf-8 -*-
#   Segregating tweet-data by users.
#   Author - Janu Verma
#   jv367@cornell.edu

import json
import sys
import urllib2



def main():
    data_file = open(sys.argv[1])
    dataByUser = {}
    for line in data_file:
        record = json.loads(line)
        user = record[0]
        if (user in dataByUser.keys()):
            if (record[4] not in dataByUser[user]['recordIDs']):
                dataByUser[user]['records'].append(record)
                dataByUser[user]['recordIDs'].append(record[4])
                dataByUser[user]['count'] += 1
        else:
            dataByUser[user] = { 'records': [record], 'count': 1, 'recordIDs': [record[4]]}
    return dataByUser
    
if __name__== '__main__':
    output = main()
    print json.dumps(output)
