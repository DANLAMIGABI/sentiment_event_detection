import re
# emoticon =""" *O *-* *O* *o* * * :P :-P :D :-D :d :-d :p :-p 8-D 8D x-D XD =3 =D B^D :-O :O :-o :o :-0 8-0 >:O :-* :* :× ;P ;D ;d ;p ;-P ;-D ;-d ;-p
#             :-) ;-) :=) ;=) :-)) :)) :^) :-3 :3 :o) :-}
#             :<) :>) ;>) ;=)
#             =} :) (: ;) ;-)
#             (; :} {: ;}
#             {; :]
#             [; :') ;') :-3
#             {; :]
#             ;-3 :-x ;-x :-X :x :X
#             ;-X :-} ;-=} :-]
#             ;-] :-.)
#             ^_^ ^-^ :( ;( :'(
#             =( ={ ): );
#             )': )'; )= }=
#             ;-{{ ;-{ :-{{ :-{
#             -/ :/ :-. >:/ :/ =/ :L =L :S
#             :-| :|
#             :-( ;-(
#             c
#             [: ;]
#             """.split()
emoticon={
    "HAPPY":[ ":-)", ";-)", ":=)", ";=)",":^)",":-3","=D",":3",":o)","^_^", "^-^",":-}",":}","{:",":]",";D",";^)",";}","{;",":-}",":-]","8-)","8)","=]",":c)",":')",":'-)"],
    "Laugh":[":D",";-D",";D",":‑D","8‑D","8D","x‑D","XD","=3","B^D"],
    "very happy":[":-))",":))"],
    "sad":[":‑(",":(",":‑c",":c",":<",":-<",":‑[",":[",":-||",">:[",":{",":@",";("],
    "angry":[">_<",">:("],
    "cry":[":'‑(",":'(",":,)",":'{"],
    "horror":["D‑':","D:<","D:","D8","D;","D=","DX"],
    "Surprise":[":‑O",":O",":‑o",":o",":-0","8‑0",">:O"],
    "Kiss":[":-*",":*",":×"],
    "cheeky":[ ":‑P",":P",";P",";d", ";p",";-P",";-d",";-p",":‑b",":b"],
    "annoy":[":‑/",":/",":‑.",">:/",":/","=/",":L","=L",":S"],
    "indecision":[":-|",":|"],
    "Embarrasse":[":$"],
    "Evil":[">:)",">:-)","}:‑)","}:)","3:)","3:-)",">;)"],
    "bored":["|‑O","|;‑)"]

}
def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                return k
    return ""
pattern2 = "|".join(map(re.escape, emoticon))
eyes, noses, mouths = r":;8BX=", r"-~'^", r")(/\|DP"
pattern1 = "[%s][%s]?[%s]" % tuple(map(re.escape, [eyes, noses, mouths]))
import csv
import pymysql
csvfile=open("D:/json_Parser/election2012/emoticon.csv",encoding='utf-8', mode='w')
writer = csv.writer(csvfile, delimiter='\t',lineterminator='\n')
import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='facup', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
cursor = cnx.cursor()
select = ("SELECT id,title FROM emojitrack WHERE publicationTime")# BETWEEN '2012-05-05 15:00:00' AND '2012-05-05 19:59:59' ")
cursor.execute(select)
ids=cursor.fetchall()
print("fetch finishe!")
i=0
id=1336044
for line in ids:
    i+=1
    emo = []
    em = ""
    smiley = []
    smiley = re.findall(pattern1, line[1])
    # print(smiley)
    for element in smiley:
        # print (element)
        emotions = search(emoticon, element)
        emo.append(emotions)
    print(emo)
    em = " ".join(emo)
    writer.writerow([em])
    # update_tweet = ("UPDATE emojitrack "
    #            "SET emoticon='%s' "
    #            "WHERE id=%s ;" % (em , line[0]))
    # cursor.execute(update_tweet)
    if(i%500==0):
        print(i)

with open("D:/json_Parser/election2012/emoticon.csv") as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        update_tweet = ("UPDATE emojitrack "
                        "SET emoti='%s' "
                        "WHERE id=%s ;" % (" ".join(row), id))
        cursor.execute(update_tweet)
        id+=1

print("finished")
cursor.close()
cnx.close()
#"ORDER BY interval_start")
#t2.`DATE` between DATE_ADD(t1.`DATE`, INTERVAL -6 DAY)
