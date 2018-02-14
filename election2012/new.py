import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='facup', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
cursor = cnx.cursor()
select = ("SELECT emoji FROM emojitrack WHERE id=1336223 ")#" WHERE publicationTime BETWEEN '2012-05-05 15:00:00' AND '2012-05-05 19:59:59' ")
cursor.execute(select)
ids=cursor.fetchone()
print("fetch finishe!")
print(ids[0])
