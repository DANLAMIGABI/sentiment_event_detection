import json
import datetime
import time
from os import listdir
from os.path import isfile, join
# $ pip install pytz
import pymysql
from datetime import datetime
import pytz
import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='election', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
path = "D:/us_election16/res/res.json"
jsonfiles=open (path,encoding='utf8',mode='r')
#outpath = "D:/json_Parser/"
cursor = cnx.cursor()
tweets_tuple = []
i = 0
for line in jsonfiles:
    line='['+line+']'
    tweets=json.loads(line)
    for tweet in tweets:
        #print(tweet)
        #tweet =(json.load())
        text = tweet['text'].replace("\r\n"," ").replace("\r"," ").replace("\n"," ").replace(","," ").replace("\t"," ")
        from dateutil import parser
        dt = parser.parse(str(tweet['created_at']))
        created = dt.astimezone(pytz.timezone('EST'))
        print(created)

        hashtags = []   #make an empty list

        for hashtag in tweet["entities"]["hashtags"]:    #iterate over the list
            hashtags.append(hashtag["text"])
        #print(hashtags)
        insert_tweet = ("INSERT INTO election17 "
                        "(text, created, tags) "
                        "VALUES (%(text)s, %(created)s, %(tags)s)")
        tweet_data = {
            'text': text,
            'created':created,
            'tags': str(hashtags),
        }
        # Insert new employee
        cursor.execute(insert_tweet, tweet_data)
        cnx.commit()
        i+=1
        if i%500 ==0:
            print(str(i))

cursor.close()
cnx.close()
print("Finish Reading File")
