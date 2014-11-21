import sys

with open(sys.argv[1]) as lines:
    a = set()
    for line in lines:
        a.add(line)
    tweets = ""
    for tweet in a:
        tweets += tweet
    print tweets
