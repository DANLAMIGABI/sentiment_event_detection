import pymysql.cursors
import pymysql
import pandas as pd
# import matplotlib.pyplot as plt
import plotly.plotly as py
from plotly.graph_objs import *
import plotly

cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='facup', charset='utf8',
                      cursorclass=pymysql.cursors.SSCursor)
cursor = cnx.cursor()
selection=("SELECT id,IntervalTime,AvgAnger,AvgDisgust,AvgFear,AvgJoy,AvgSadness,AvgSurprise,NegFreq,PosFreq,cnt FROM emotiontoken")
cursor.execute(selection)
resultset=cursor.fetchall()
# id=[]
# IntervalTime=[]
# AvgAnger=[]
# AvgDisgust=[]
# AvgFear=[]
# AvgJoy=[]
# AvgSadness=[]
# AvgSurprise=[]
# #
df = pd.DataFrame( [[ij for ij in i] for i in resultset] )
df.rename(columns={0: 'id', 1: 'IntervalTime', 2: 'AvgAnger', 3: 'AvgDisgust', 4:'AvgFear' ,5:'AvgJoy',6:'AvgSadness',7:'AvgSurprise',8:'NegFreq',9:'PosFreq',10:'cnt'}, inplace=True);
df = df.sort_values (['IntervalTime'], ascending=[1])
# df = df.cumsum()
# for rows in resultset:
#     id.append(rows[0])
#     IntervalTime.append(rows[1])
#     AvgAnger.append(rows[2])
#     AvgDisgust.append(rows[3])
#     AvgFear.append(rows[4])
#     AvgJoy.append(rows[5])
#     AvgSadness.append(rows[6])
#     AvgSurprise.append(rows[7])

trace1 = Scatter(
    y=df['AvgAnger'],
    x=df['IntervalTime'],
    # text=country_names,
    # mode='markers'
)
trace2 = Scatter(
    y=df['AvgDisgust'],
    x=df['IntervalTime'],
)
trace3 = Scatter(
    y=df['AvgFear'],
    x=df['IntervalTime'],
)
trace4 = Scatter(
    y=df['AvgJoy'],
    x=df['IntervalTime'],
)
trace5 = Scatter(
    y=df['AvgSadness'],
    x=df['IntervalTime'],
)
trace6 = Scatter(
    y=df['AvgSurprise'],
    x=df['IntervalTime'],
)
trace7= Scatter(
    y=df['NegFreq'],
    x=df['IntervalTime'],
    mode='markers',
)

trace8=Scatter(
    y=df['PosFreq'],
    x=df['IntervalTime'],
    mode='markers',
)
trace9=Scatter(
    y=df['cnt'],
    x=df['IntervalTime'],
    mode='markers',
    line = dict(
            color = ('rgb(22, 96, 167)'),
            width = 4,
            dash = 'dot')
)

layout = Layout(
    xaxis=XAxis( title='IntervalTime')
)
data = Data([trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8,trace9])
fig = Figure(data=data, layout=layout)
plotly.tools.set_credentials_file(username='shivashadrooh', api_key='NrwOQVTz4X7BItBKffSU')
# plotly API_key="NrwOQVTz4X7BItBKffSU"
py.iplot(fig, filename='Avg of anger in time intervals')
