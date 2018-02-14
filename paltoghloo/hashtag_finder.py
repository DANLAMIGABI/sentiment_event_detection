import pymysql.cursors
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import math
from nltk.tokenize import sent_tokenize, word_tokenize
import re, string
regex2= re.compile("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)") #just keep alphabetic values
stops = set(stopwords.words('english'))
stops.add("rt")
lemma = nltk.wordnet.WordNetLemmatizer()
# from textblob import TextBlob
# cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='facup', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
# cursor = cnx.cursor()
# keyword="'%win%'"
# select_goal_hashtags="SELECT publicationTime,title,tags FROM football WHERE tags like "+keyword+""
# cursor.execute(select_goal_hashtags)
# resultset= cursor.fetchall()
# insert_tweet = ("INSERT INTO win "
#                 "(pubTime, title, tags, nltk) "
#                 "VALUES (%(pubTime)s, %(title)s, %(tags)s, %(nltk)s)")

ii="i went to tehran"
for tuple in ii:
    line = regex2.sub('', tuple[1])
    stringer = nltk.word_tokenize(line)
    tmp = []
    for w in stringer:
        word = w.lower()
        word1=lemma.lemmatize(word)
        if len(word) == 0 or word in stops:
            continue
        tmp.append(word1)

    text = " ".join(tmp)
    print(text)
    testimonial = TextBlob(text)
    value = testimonial.polarity
    tweet_data = {
        'pubTime':tuple[0],
        'title': tuple[1],
        'tags': tuple[2],
        'nltk': value,
    }
    # Insert new employee
    cursor.execute(insert_tweet, tweet_data)
    cnx.commit()
    print(value)
print("done!")
cursor.close()
# tweets_tuple.append((title, publicationTime, tags))
# cursor.execute(select_top20)
