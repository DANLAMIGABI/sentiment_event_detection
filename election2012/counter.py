import json
import datetime
import time
from os import listdir
from os.path import isfile, join
# $ pip install pytz
import pymysql
from datetime import datetime
import pytz
import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='election12', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
path = "D:/us_election/"
#outpath = "D:/json_Parser/"
jsonfiles = [f for f in listdir(path) if isfile(join(path, f))]
cursor = cnx.cursor()
tweets_tuple = []
i = 0
cnt=0
for file in jsonfiles:
    for line in file:
        cnt+=1
        print(line)
    i+=1
print(i)
print(cnt)
