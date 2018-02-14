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
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='fullelection12', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
path = "D:/all datasets/election2012 full dataset/extracted/"
#outpath = "D:/json_Parser/"
jsonfiles = [f for f in listdir(path) if isfile(join(path, f))]
cursor = cnx.cursor()
tweets_tuple = []
i = 0

for file in jsonfiles:

    f = open(path+file, encoding='utf-8', mode='r')
    print(path+file)

    for line in f:
        i = i + 1
        print(i)
        if (i < 18158315):
            continue
        try:
            tweet = json.loads(line)
            text = tweet['text'].replace("\r\n", " ").replace("\r", " ").replace("\n", " ").replace(",", " ").replace("\t"," ")

            from dateutil import parser

            dt = parser.parse(str(tweet['created_at']))
            created = dt.astimezone(pytz.timezone('EST'))
            # print(created)

            hashtags = []  # make an empty list

            for hashtag in tweet["entities"]["hashtags"]:  # iterate over the list
                hashtags.append(hashtag["text"])
            # print(hashtags)
            insert_tweet = ("INSERT INTO elec12 "
                            "(text, created, tags) "
                            "VALUES (%(text)s, %(created)s, %(tags)s)")
            tweet_data = {
                'text': text,
                'created': created,
                'tags': str(hashtags),
            }
            # Insert new employee
            cursor.execute(insert_tweet, tweet_data)
            cnx.commit()
        except:
            print("skip!")

        #retweetCount=int(tweet['retweetCount'].__str__()[:-3])
cursor.close()
cnx.close()
print("Finish Reading File")
