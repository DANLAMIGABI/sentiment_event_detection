import csv
import pymysql
import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='facup', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
cursor = cnx.cursor()
select_tweet_2min = ("SELECT  pubTime as interval_start, "
                     "AVG(CASE WHEN nltk > 0 THEN nltk ELSE 0 END)as positiveSentiment, "
                     "AVG(CASE WHEN nltk < 0 THEN nltk ELSE 0 END)as negativeSentiment "
                     "FROM goal "
                     "GROUP BY UNIX_TIMESTAMP(pubTime) DIV 60")

select_tweet_5min2=("SELECT t1.pubTime ,"
                    "AVG(CASE WHEN t2.nltk > 0 THEN t2.nltk ELSE 0 END)as positiveSentiment, "
                    "AVG(CASE WHEN t2.nltk < 0 THEN t2.nltk ELSE 0 END)as negativeSentiment "
                    "FROM goal t1 "
                    "left OUTER JOIN goal t2 "
                    "ON t2.pubTime BETWEEN DATE_ADD(t1.pubTime, INTERVAL +5 MINUTE ) "
                    "AND t1.pubTime "
                    "GROUP BY t1.pubTime")
                     #"ORDER BY interval_start")
#t2.`DATE` between DATE_ADD(t1.`DATE`, INTERVAL -6 DAY)
cursor.execute(select_tweet_2min)
print("negative\n")
rows=[]
with open("D:/json_Parser/tokenSpikes4.csv",encoding='utf-8', mode='w') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    rows=cursor.fetchall()
    for tweets in rows:
        writer.writerow(['', tweets[0],tweets[1],tweets[2]])
        print(str(tweets[0]))
        #print(str(tweets[2]))
#
#
# insert_tweet = ("INSERT INTO paltgoal "
#                 "(posAvg, negAvg, timing ) "
#                 "VALUES (%(posAvg)s, %(negAvg)s, %(timing)s)")
# for row in rows:
#     tweet_data = {
#     'posAvg':row[1] ,
#     'negAvg': row[2],
#     'timing': row[0],
# }
#     cursor.execute(insert_tweet,tweet_data)
#     cnx.commit()

cursor.close()
cnx.close()
csvfile.close()
