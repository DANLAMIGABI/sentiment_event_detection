import csv
import pymysql
import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='facup', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
cursor = cnx.cursor()
select_tweet_5min = ("SELECT  publicationTime as interval_start,"
                     "AVG(sentiScore) as sentiment "
                     "FROM football "
                     "GROUP BY UNIX_TIMESTAMP(publicationTime) DIV 300")
                     #"ORDER BY interval_start")
cursor.execute(select_tweet_5min)
with open("D:/json_Parser/tokenSpikes.csv",encoding='utf-8', mode='w') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    for tweets in cursor.fetchall():
        writer.writerow(['', tweets[0],tweets[1]])
        print(str(tweets[0]))




cnx.commit()
cursor.close()
cnx.close()

