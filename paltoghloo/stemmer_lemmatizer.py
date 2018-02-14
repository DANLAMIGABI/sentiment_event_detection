import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import math
import re, string
from stemming.porter2 import stem
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
from nltk.stem.snowball import SnowballStemmer
wnl = WordNetLemmatizer()

text="i went tiring to tehran @yahoo.com #shiva continually books leaves"

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




print(' '.join(lemma_text))
