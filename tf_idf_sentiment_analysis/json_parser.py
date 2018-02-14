import json
tweets_tuple = []
import datetime
import csv
import string
import nltk
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import wordnet
from textblob import TextBlob
from os import listdir
from os.path import isfile, join
import pymysql
import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='facup', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
path = "D:/facup_arranged/"
outpath = "D:/json_Parser/"
jsonfiles = [f for f in listdir(path) if isfile(join(path, f))]

tweets_tuple = []
i = 0;

for file in jsonfiles:
    f = open(path+file, encoding='utf-8', mode='r')
    for line in f:
        tweet = json.loads(line)
        title = tweet['title'].replace("\r\n"," ").replace("\r"," ").replace("\n"," ").replace(","," ").replace("\t"," ")
        for w in title:
            if not wordnet.synsets(w):
                title.replace(w,"")
                print(w)
        publicationTime = int(tweet['publicationTime'].__str__()[:-3])
        tags=tweet['tags']
        testimonial = TextBlob(str(title))
        value = testimonial.polarity
        cursor = cnx.cursor()

        insert_tweet = ("INSERT INTO football "
                        "(title, publicationTime, tags, sentiScore) "
                        "VALUES (%(title)s, %(publicationTime)s, %(tags)s, %(sentiScore)s)")
        tweet_data = {
            'title': title,
            'publicationTime': datetime.datetime.utcfromtimestamp(publicationTime).strftime('%Y-%m-%d %H:%M:%S') ,
            'tags': str(tags),
            'sentiScore': value,
        }
        # Insert new employee
        cursor.execute(insert_tweet, tweet_data)
        cnx.commit()
        cursor.close()
        tweets_tuple.append((title, publicationTime, tags))

        #retweetCount=int(tweet['retweetCount'].__str__()[:-3])

    i = i + 1
    if (i % 500 == 0):
        print(i)
cnx.close()
print("Finish Reading File")

tweets_tuple_sorted = sorted(tweets_tuple, key=lambda tuple: tuple[1])   # sort by timestamp
with open("D:/json_Parser/facupdataset.csv",encoding='utf-8', mode='w') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    for tuple in tweets_tuple_sorted:
        time = datetime.datetime.utcfromtimestamp(tuple[1]).strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow(['',time,tuple[0],tuple[2]])


print("DONE !!!")

f.close()
