import nltk
from nltk.corpus import stopwords
import math
from nltk.tokenize import sent_tokenize, word_tokenize
import re, string
from collections import Counter


#regex = re.compile('[^a-zA-Z ]') #just keep alphabetic values
####################################################TF_IDF###################################
def tf(word, line):
    words = line.split()
    wordCount = Counter(words)
    #print()
    a = re.split(r'\W',line)
    return a.count(word) / wordCount[word]

def n_containing(word, doc):
    c=0
    for line in doc:
        words = line.split()
        if word in words:
            c+=1
    return c


def idf(word, doc):
    return math.log1p(len(doc) / (1 + n_containing(word, doc)))

def tfidf(word,line, doc):
    return tf(word, line) * idf(word, doc)
#########################################END##################################################
regex2= re.compile("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)") #just keep alphabetic values
stops = set(stopwords.words('english'))
stops.add("rt")
word_list = open("../results/tweets title.txt", "r")
filtered_words=[]
for line in word_list.readlines():
    line = regex2.sub('', line)
    stringer=nltk.word_tokenize(line)
    tmp=[]
    for w in stringer:
        word=w.lower()
        #word=regex.sub('',word)
        #word=regex2.sub('',word)
        if len(word)==0 or word in stops :
            continue
        tmp.append(word)

    filtered_words.append(" ".join(tmp))#list of formatted tweet
print(filtered_words)
doc1=(line for line in filtered_words)
i=0
##############################################################################################
for line in filtered_words:
        print(line)
        print("Top words in document {}".format(i + 1))
        i+=1
        scores = {word: tfidf(word, line, filtered_words) for word in line.split()}
        print(scores)
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:2]:
            print("\tWord: {}, TF-IDF: {}".format(word,round(score, 5)))
