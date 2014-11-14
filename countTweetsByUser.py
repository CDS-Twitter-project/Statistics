#note: this script should be run on the output of segregateByUsers.py

import sys
import json
import operator

def main():
    data_file = open(sys.argv[1])
    dataByUser = []
    records = json.loads(data_file.readline())
    for usr in records:
        dataByUser.append({'user': usr, 'count': records[usr]['count']})
    return dataByUser
    
if __name__== '__main__':
    output = main()
    output.sort(key=operator.itemgetter('count'), reverse=True)
    print json.dumps(output)
