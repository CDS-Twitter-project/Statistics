Statistics
==========

This repo contains statistics computed after analyzing data from twitter. 

The statistics will be used to create visualizations, further analysis and for machine learning models. 

#########################################
dataExtraction.py - run this on your json files (what you got from API calls). This will extract relevant info from the json tweets.

        python dataExtraction.py [JSON_FILE] > [my_file]

The output for each tweet will be of this form (a JSON encoded list). 

      [user_id, text, fav_count, retweets, index, date, hashtags]
      
      
segregationByUsers.py and segregationByDate.py runs on the [my_file] and clubs the tweets based on data/user. 

top_hashtags.py runs on the [JSON_FILE] to compute top hashtags in the file. 

pop_words.py runs on the [my_file] and compute top n most frequent words in the file. 





      
    


