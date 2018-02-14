
import  json
path = "D:/us_election16/res/res.json"
jsonfiles=open (path,encoding='utf8',mode='r')
tweets=[]
for line in jsonfiles:
    line='['+line+']'
    js=json.loads(line)
    for j in js:
        print(j['created_at'])
    break
