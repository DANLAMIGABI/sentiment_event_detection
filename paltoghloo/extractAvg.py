#tweet between time 16:00 to 18:15 5/5/2012
import csv
import pymysql
import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='facup', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
cursor = cnx.cursor()
cursor2 = cnx.cursor()
cursor3 = cnx.cursor()
id_extractor=("SELECT id FROM tk2")
cursor.execute(id_extractor)
ids=cursor.fetchall()
for i in ids:
    print(i[0])
    avg_neg = ("SELECT avg(t.NegFreq) FROM (SELECT NegFreq FROM tk2 WHERE id<='%s' ORDER BY id DESC LIMIT 2) t ;" % i[0])
    cursor2.execute(avg_neg)
    avgneg=cursor2.fetchone()
    print(avgneg)
    avg_pos = ("SELECT avg(t2.PosFreq) FROM (SELECT PosFreq FROM tk2 WHERE id<='%s' ORDER BY id DESC LIMIT 2) t2 ;" % i[0])
    cursor3.execute(avg_pos)
    avgpos =cursor3.fetchone()
    print(avgpos)
    # insert_tweet = ("INSERT INTO tokenspikes "
    #                 "(PosAvg, NegAvg ) "
    #                 "VALUES (%(PosAvg)s, %(NegAvg)s)")
    update_tweet=("UPDATE tk2 "
                  "SET PosAvg=%s, NegAvg=%s WHERE id='%s'" %(avgpos[0],avgneg[0],i[0]) )
#("UPDATE tblTableName SET Year=%s, Month=%s, Day=%s, Hour=%s, Minute=%s WHERE Server='%s' " % (Year, Month, Day, Hour, Minute, ServerID)
    cursor.execute(update_tweet)
    #cnx.commit()
cursor.close()
cursor2.close()
cursor3.close()
cnx.close()
