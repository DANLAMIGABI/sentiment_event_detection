import nltk
from nltk.corpus import stopwords
import math
from textblob import TextBlob as tb
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import re, string
ps = PorterStemmer() #stemming
#######################################################
def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log1p(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

def removearticles(text):
  re.sub('\s+(a|an|and|the|rt|for|of|)(\s+)', '\2', text)
###############################################################END OF TF_IDF FUNCTION##################################################
word_list = open("results/tweets title.txt", "r")
stops = set(stopwords.words('english'))
#print(stops)
# ...
#filtered_words = [word for word in word_list if word.lower() not in stops] #delete stop words
filtered_words=[]
for line in word_list.readlines():
    stringer=nltk.word_tokenize(line)
    print(stringer)
    exit()

regex = re.compile('[^a-zA-Z ]') #just keep alphabetic values
text_file = open("append.txt", "r+")
for line in filtered_words:
    word = regex.sub('',line.lower())
    #removearticles(word)
    text_file.write(word)
    print(word)
clean_text=text_file.read().lower()
text_file.close()
words = word_tokenize(clean_text)
######################################################################END OF DELETE STOPWORDS AND lowercase ############################
document1=tb(clean_text)
bloblist = [document1]
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    print(scores)
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:10]:
        print("\tWord: {}, TF-IDF: {}".format(word,round(score, 5)))
