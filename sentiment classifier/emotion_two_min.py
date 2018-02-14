import pymysql.cursors
import  pymysql
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='facup', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
cursor = cnx.cursor()
cursor2= cnx.cursor()
cursor3= cnx.cursor()
sec="120"
table_hashtag="goal"
table_affected="emotiontoken"
select_tweet_2min = ("SELECT  pubTime ,"
                     "COUNT(*) AS cnt , "
                     "SUM(nltk>0) as pos, "
                     "SUM(nltk<0) as neg , "
                     "SUM(Anger), "
                     "SUM(Disgust), "
                     "SUM(Fear), "
                     "SUM(Joy), "
                     "SUM(Sadness), "
                     "SUM(Surprise) "
                     "FROM "+table_hashtag+" "
                     "WHERE pubTime BETWEEN '2012-05-05 16:00:01' AND '2012-05-05 18:15:00'"
                     "GROUP BY UNIX_TIMESTAMP(pubTime) DIV "+sec+"")

#tweet emotions is in goal table

truncate=("DELETE FROM "+table_affected+" ")
                     #"ORDER BY interval_start")
#"COUNT(CASE WHEN nltk > 0 THEN nltk ELSE 0 END)as pos ,"
#"COUNT(CASE WHEN nltk < 0 THEN nltk ELSE 0 END)as neg "

cursor.execute(select_tweet_2min)
cursor2.execute(truncate)
result_set=cursor.fetchall()
insert_tweet = ("INSERT INTO emotiontoken "
                    "( IntervalTime, cnt, PosFreq, NegFreq,AvgAnger,AvgDisgust,AvgFear,AvgJoy,AvgSadness,Avgsurprise ) "
                    "VALUES (%(IntervalTime)s, %(cnt)s, %(PosFreq)s, %(NegFreq)s, %(AvgAnger)s, %(AvgDisgust)s ,%(AvgFear)s,%(AvgJoy)s,%(AvgSadness)s,%(Avgsurprise)s)")

for row in result_set:
    tweet_data = {
        'IntervalTime': row[0],
        'cnt': row[1],
        'PosFreq':row[2]/row[1]*100, #average of pos frequences each 2min
        'NegFreq':row[3]/row[1]*100, #average of neg frequences each 2min
        'AvgAnger':row[4],
        'AvgDisgust':row[5],
        'AvgFear':row[6],
        'AvgJoy':row[7],
        'AvgSadness':row[8],
        'Avgsurprise':row[9],

    }
    cursor3.execute(insert_tweet, tweet_data)
    cnx.commit()
cursor.close()
cursor2.close()
cursor3.close()
cnx.close()
