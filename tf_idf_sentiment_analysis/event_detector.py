#1)first estimate 20 max values from tweets
#2)then consider 5min below and 5min after that time to extrat posts
#3)then try to extact common keywords using freQuent pattern extraction or keyword extraction method
#1)
import pymysql
import csv
import re
import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='facup', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
cursor = cnx.cursor()
select_top20="SELECT PosAvg,FiveMin FROM sentiavg ORDER BY PosAvg desc limit 20"
cursor.execute(select_top20)
with open("D:/json_Parser/top20Positive.csv", encoding='utf-8', mode='w') as csvfile1:
    writer = csv.writer(csvfile1, delimiter='\t')
    for row in cursor.fetchall():
        writer.writerow(['', row[0], row[1]])
print("\n ended positive\n")
select_top20="SELECT NegAvg,FiveMin FROM sentiavg ORDER BY NegAvg ASC limit 20"
cursor.execute(select_top20)
fivemin=[]
with open("D:/json_Parser/top20Negative.csv", encoding='utf-8', mode='w') as csvfile2:
        writer = csv.writer(csvfile2, delimiter='\t')
        for row1 in cursor.fetchall():
            writer.writerow(['', row1[0], row1[1]])
            fivemin=row1[1]


select_negative_posts="SELECT title FROM football WHERE publicationTime BETWEEN (%(val1)s) AND (%(val1)s + INTERVAL 5 MINUTE)"
select_data={
    'val1':fivemin.strftime('%Y-%m-%d %H:%M:%S') ,
        #fivemin.strftime('%Y-%m-%d %H:%M:%S'),
}

cursor.execute(select_negative_posts,select_data)
for tweets in cursor.fetchall():
    tweets=re.sub(r"http\S+", "", str(tweets),flags=re.MULTILINE)
    print(tweets+"\n")
#select_positive_posts=

cursor.close()
cnx.close()
