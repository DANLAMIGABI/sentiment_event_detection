import unicodedata as ud
import csv
csvfile=open("D:/json_Parser/election2012/emoji.csv",encoding='utf-8', mode='w')
writer = csv.writer(csvfile, delimiter='\t',lineterminator='\n')
import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='facup', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
cursor = cnx.cursor()
select = ("SELECT emoji FROM emojitrack ORDER BY id ASC ")#" WHERE publicationTime BETWEEN '2012-05-05 15:00:00' AND '2012-05-05 19:59:59' ")
cursor.execute(select)
ids=cursor.fetchall()
print("fetch finishe!")

for line in ids:
    em = ""
    emo=[]
    print(line[0])
    #for c in line[1]:
        #print('{} U+{:5X} {}'.format(c, ord(c), ud.name(c)))
        #emo.append('{} U+{:5X} {}'.format(c, ord(c), ud.name(c)))
    #em=" ".join(emo)
    writer.writerow([em])
    # update_tweet = ("UPDATE emojitrack "
    #            "SET emoticon='%s' "
    #            "WHERE id=%s ;" % (em , line[0]))
    # cursor.execute(update_tweet)
print("finished")
cursor.close()
cnx.close()
