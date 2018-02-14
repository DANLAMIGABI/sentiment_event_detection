#tweet between time 16:00 to 18:15 5/5/2012
import csv
import pymysql
import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='facup', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
cursor = cnx.cursor()
sec="120"
select_tweet_2min = ("SELECT  pubTime ,title,nltk ,"
                     "COUNT(*) AS cnt , "
                     "SUM(nltk>0) as pos, "
                     "SUM(nltk<0) as neg "
                     "FROM win "
                     "WHERE pubTime BETWEEN '2012-05-05 16:00:01' AND '2012-05-05 18:15:00'"
                     "GROUP BY UNIX_TIMESTAMP(pubTime) DIV "+sec+"")
                     #"ORDER BY interval_start")
#"COUNT(CASE WHEN nltk > 0 THEN nltk ELSE 0 END)as pos ,"
#"COUNT(CASE WHEN nltk < 0 THEN nltk ELSE 0 END)as neg "

cursor.execute(select_tweet_2min)
result_set=cursor.fetchall()
insert_tweet = ("INSERT INTO tk2 "
                    "(title, nltk, 2minTime, cnt, PosFreq, NegFreq ) "
                    "VALUES (%(title)s, %(nltk)s, %(2minTime)s, %(cnt)s, %(PosFreq)s, %(NegFreq)s)")

for row in result_set:
    tweet_data = {
        'title': row[1],
        'nltk': row[2],
        '2minTime': row[0],
        'cnt':row[3],
        'PosFreq':row[4]/row[3]*100, #average of pos frequences each 2min
        'NegFreq':row[5]/row[3]*100, #average of neg frequences each 2min
    }
    cursor.execute(insert_tweet, tweet_data)
    cnx.commit()
cursor.close()
cnx.close()
