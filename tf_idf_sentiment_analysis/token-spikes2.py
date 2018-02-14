import csv
import pymysql
import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='facup', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
cursor = cnx.cursor()
select_tweet_5min = ("SELECT  publicationTime as interval_start, "
                     "AVG(CASE WHEN sentiScore > 0 THEN sentiScore ELSE 0 END)as positiveSentiment, "
                     "AVG(CASE WHEN sentiScore < 0 THEN sentiScore ELSE 0 END)as negativeSentiment, "
                     "AVG(sentiScore) as sentiment "
                     "FROM football "
                     "GROUP BY UNIX_TIMESTAMP(publicationTime) DIV 60")
                     #"ORDER BY interval_start")
cursor.execute(select_tweet_5min)
print("positive\n")
rows=[]
with open("D:/json_Parser/tokenSpikes2.csv",encoding='utf-8', mode='w') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    rows=cursor.fetchall()
    for tweets in cursor.fetchall():
        writer.writerow(['', tweets[0],tweets[1],tweets[2],tweets[3]])
        print(str(tweets[2]))
        #print(str(tweets[2]))

cursor.close()


for row in rows:
    cursor = cnx.cursor()
    insert_tweet = ("INSERT INTO sentiAvg "
                    "(PosAvg, NegAvg, FiveMin ) "
                    "VALUES (%(PosAvg)s, %(NegAvg)s, %(FiveMin)s)")
    tweet_data = {
    'PosAvg':row[1] ,
    'NegAvg': row[2],
    'FiveMin': row[0],
}
    cursor.execute(insert_tweet,tweet_data)
    cnx.commit()
    cursor.close()
cnx.close()
