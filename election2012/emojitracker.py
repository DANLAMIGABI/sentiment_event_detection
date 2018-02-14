import emoji
import re
emoticon = ["*O", "*-*", "*O*", "*o*", "* *",
            ":P",":-P", ":D",":-D", ":d", ":-d", ":p",":-p" ,"8‑D", "8D", "x‑D","XD","=3","=D","B^D",
            ":‑O",":O",":‑o",":o",":-0","8‑0",">:O",
            ":-*",":*",":×","","",
            ";P", ";D", ";d", ";p",";-P", ";-D", ";-d", ";-p",
            ":-)", ";-)", ":=)", ";=)",":-))",":))",":^)",":-3","=D",":3",":o)",":-}",
            ":<)", ":>)", ";>)", ";=)",
            "=}", ":)", "(:;)",";-)",
            "(;", ":}", "{:", ";}",
            "{;:]",
            "[;", ":')", ";')", ":-3",
            "{;", ":]",
            ";-3", ":-x", ";-x", ":-X",":x",":X",
            ";-X", ":-}", ";-=}", ":-]",
            ";-]", ":-.)",
            "^_^", "^-^",":(", ";(", ":'(",
            "=(", "={", "):", ");",
            ")':", ")';", ")=", "}=",
            ";-{{", ";-{", ":-{{", ":-{",
            "‑/",":/",":‑.",">:/",":/","=/",":L","=L",":S",
            ":-|",":|",
            ":-(", ";-(",
            ":,)", ":'{",
            "[:", ";]"
            ]
def extract_emotion(str):
    return ' '.join(c for c in str if c in emoticon)
def extract_emojis(str):
  return ' '.join(c for c in str if c in emoji.UNICODE_EMOJI)
import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='election', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
cursor = cnx.cursor()
cursor2 =cnx.cursor()
select="SELECT id, text FROM election17"
cursor.execute(select)
resultset=cursor.fetchall()
print("fetch finished!")
i=0
for line in resultset:
  emojis = []
  emoticons=[]
  i+=1
  print(i)
  #print(line[0])
  #print(line[1])
  # for c in line[1]:
  #   print(line[0])
  #   if c in emoji.UNICODE_EMOJI:
  #     ''.join()
  emojis =extract_emojis(str(line[1]))
 # emoticons=extract_emotion(str(line[1]))
  print(emojis)
  #print(emoticons)
  update_tweet = ("UPDATE election17 "
                      "SET emoji='%s' "
                      "WHERE id=%s ;" %(emojis, line[0]))
  #update_tweet = ("INSERT INTO emojitrack "
  #                "(emoji) "
  #                "VALUE ('%s') "
  #                "WHERE id='%s'" %(str(emojis),line[0]))
  cursor2.execute(update_tweet)
  #cnx.commit()
  #print("success")

print("finished!")
cursor.close()
cursor2.close()
cnx.close()





# def is_emoji(s):
#     count = 0
#     for emoji in UNICODE_EMOJI:
#         count += s.count(emoji)
#         if count > 1:
#             return False
#     return bool(count)

