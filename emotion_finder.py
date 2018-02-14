import pymysql.cursors
cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='facup', charset='utf8',cursorclass = pymysql.cursors.SSCursor)
from emotion_predictor import EmotionPredictor
import pandas as pd
import operator
import nltk
from nltk.corpus import stopwords
import math
import re, string
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
from nltk.stem.snowball import SnowballStemmer


def cleaner(text):
    wnl = WordNetLemmatizer()

    regex2= re.compile("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)") #just keep alphabetic values
    compiled_text=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",text).split())

    # 1)stopword remover
    stops = set(stopwords.words('english'))
    stops.add("rt")
    lemma_text=[]
    stemmer = SnowballStemmer("english")

    # 2)lemmatize
    lemma = WordNetLemmatizer()
    tokens = nltk.word_tokenize(compiled_text.lower())
    tagged = nltk.pos_tag(tokens)
    for word,pos in tagged:
        print(pos[0])
        wntag = pos[0].lower()
        # wntag = wntag if wntag in ['a', 'r', 'n', 'v']
        if wntag in ['a', 'n', 'v']:
            lemma2 = lemma.lemmatize(word, pos=wntag)
            lemma_text.append(lemma2)
        elif wntag in ['r']:
            lemma2 = stemmer.stem(word)
            lemma_text.append(lemma2)

        else:
            wntag=None
            lemma2 = word
            lemma_text.append(lemma2)
    return (' '.join(lemma_text))


# Pandas presentation options
pd.options.display.max_colwidth = 150   # show whole tweet's content
pd.options.display.width = 200          # don't break columns
#
# Predictor for Ekman's emotions in multiclass setting.
model = EmotionPredictor(classification='ekman', setting='mc', use_unison_model=True)
cursor = cnx.cursor()
cursor2 = cnx.cursor()
cursor3 = cnx.cursor()
select_text=("SELECT id,title FROM goal ")
cursor.execute(select_text)
result=cursor.fetchall()
dictlist=[]
ids=[]
i=1
for items in result:
    dictlist.append(cleaner(items[1]))
    ids.append(items[0])
    print(i)
    i+=1

emotion_list = []
probabilities = model.predict_probabilities(dictlist)
print("classifier start working:  ")
# Anger Disgust Fear Joy Sadness Surprise
# predict lists for identifyed emotions
model_emotion_Anger= probabilities['Anger']
Anger_list=probabilities.iloc[:, 1].tolist()
model_emotion_Disgust= probabilities['Disgust']
Disgust_list=probabilities.iloc[:, 2].tolist()
model_emotion_Fear= probabilities['Fear']
Fear_list=probabilities.iloc[:, 3].tolist()
model_emotion_Joy= probabilities['Joy']
Joy_list=probabilities.iloc[:, 4].tolist()
model_emotion_Sadness= probabilities['Sadness']
Sadness_list=probabilities.iloc[:, 5].tolist()
model_emotion_Surprise= probabilities['Surprise']
Surprise_list=probabilities.iloc[:, 6].tolist()

# insert emotions predictions to database
counter=0
for id in ids:
    update_tweet=("UPDATE goal "
                      "SET Anger=%s, Disgust=%s , Fear=%s, Joy=%s, Sadness=%s, Surprise=%s WHERE id='%s'" %(int(round(Anger_list[counter]*100)),
                                                                                                            int(round(Disgust_list[counter]*100)),
                                                                                                            int(round(Fear_list[counter]*100)),
                                                                                                            int(round(Joy_list[counter]*100)),
                                                                                                            int (round(Sadness_list[counter]*100)),
                                                                                                            int(round(Surprise_list[counter]*100)),
                                                                                                            id ) )
    #("UPDATE tblTableName SET Year=%s, Month=%s, Day=%s, Hour=%s, Minute=%s WHERE Server='%s' " % (Year, Month, Day, Hour, Minute, ServerID)
    cursor.execute(update_tweet)
    counter+=1
    print(counter)
        #cnx.commit()

#create a new table named Goal_2min and compute average of each of emotions for every 2mins:

cursor.close()
cursor2.close()
cursor3.close()
cnx.close()




