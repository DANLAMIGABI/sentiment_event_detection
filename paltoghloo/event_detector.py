import csv
import pymysql
import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='facup', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
cursor = cnx.cursor()
cursor2 = cnx.cursor()
cursor3 = cnx.cursor()
cursor4=cnx.cursor()
id_extractor=("SELECT id FROM tk2")
cursor.execute(id_extractor)
ids=cursor.fetchall()
threshold=4
PosEvent=0
NegEvent=0
cntNeg=0
cntPos=0
for i in ids:
    print(i[0])
    if i[0] == 161:
        print("skip")
        continue
    pos_select_Freq=("SELECT PosFreq,NegFreq FROM tk2 WHERE  id='%s';" %i[0])
    cursor2.execute(pos_select_Freq)
    f1=cursor2.fetchone()
    PosFreq=f1[0]
    NegFreq =f1[1]
    id2=i[0]-1
    print(id2)
    pos_avg=("SELECT PosAvg,NegAvg FROM tk2 WHERE  id='%s';" %id2)
    cursor3.execute(pos_avg)
    f2 = cursor3.fetchone()
    print(f2)
    PosAvg=f2[0]
    NegAvg=f2[1]
    if (round(PosFreq) >= threshold * round(PosAvg)):
        PosEvent=1
        cntPos+=1
    elif (round(PosFreq) < threshold * round(PosAvg)):
        PosEvent=0
    if (round(NegFreq) >= threshold * round(NegAvg)):
        NegEvent=1
        cntNeg+=1
    elif(round(NegFreq) < threshold * round(NegAvg)):
        NegEvent=0


            #                 "VALUES (%(PosAvg)s, %(NegAvg)s)")
    update_tweet = ("UPDATE tk2 "
                    "SET PosEvent=%s, NegEvent=%s WHERE id='%s'" % (PosEvent, NegEvent, i[0]))
    # ("UPDATE tblTableName SET Year=%s, Month=%s, Day=%s, Hour=%s, Minute=%s WHERE Server='%s' " % (Year, Month, Day, Hour, Minute, ServerID)
    cursor.execute(update_tweet)
    # cnx.commit()

print("negative count of goals: "+ str(cntNeg))
print("positive count of goals: "+ str(cntPos))
goal_finder = ("SELECT 2minTime From tk2 WHERE PosEvent=1 ")
cursor4.execute(goal_finder)
print("positive spikes: ")
for row in cursor4.fetchall():
    print(row[0])
goal_finder1 = ("SELECT 2minTime From tk2 WHERE NegEvent=1 ")
cursor3.execute(goal_finder1)
print("negative spikes: ")
for row1 in cursor3.fetchall():
    print(row1[0])
cursor.close()
cursor2.close()
cursor3.close()
cursor4.close()
cnx.close()
