import string
import nltk
from textblob import TextBlob
import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='facup', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
cursor = cnx.cursor()

select_tweet = ("SELECT title FROM goal")
insert_score = ("INSERT INTO goal "
                "(nltk) "
                "VALUES (%(nltk)s)")
cursor.execute(select_tweet)
resultset=cursor.fetchall()
for row in resultset:
    print(row)
    text=row
    testimonial=TextBlob(str(text))
    value = testimonial.polarity
    inser_data = {'nltk': value}
    cursor.execute(insert_score,inser_data)
    print(value)
cursor.close()
cnx.close()
