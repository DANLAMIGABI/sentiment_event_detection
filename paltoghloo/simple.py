import csv
import pymysql
import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='facup', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
cursor = cnx.cursor()
select_tweet_2min = ("SELECT  id,pubTime FROM goal limit 40")
cursor.execute(select_tweet_2min)
result=list(cursor.fetchall())
listed=list(result)
Id=[]
Title=[]
body=[]
for line in result:
    Id.append(line[0])
    Title.append(line[1])
print(Id)
print(Title)
print(listed)
print(len(listed))
