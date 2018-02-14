from rake_nltk import Rake

r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.
data = ()
from nltk.corpus import stopwords
word_list = open("results/tweets title.txt", "r")
stops = set(stopwords.words('english'))
# ...
filtered_words = [word for word in word_list if word not in stops]
import re, string
regex = re.compile('[^a-zA-Z ]')
text_file = open("append.txt", "r+")
for line in filtered_words:
    word = regex.sub('',line)
    text_file.write(word)
    print(word)
clean_text=text_file.read()
text_file.close()
#d_list:
#     for w in line.split():
#         if w.lower() not in stops:
#             print w
#r = Rake(<language>) # To use it in a specific language supported by nltk.

# If you want to provide your own set of stop words and punctuations to
# r = Rake(<list of stopwords>, <string of puntuations to ignore>)

r.extract_keywords_from_text(clean_text)
print("\n")
r.get_word_degrees()
print(r.get_word_degrees() )
#get_ranked_phrases()[:5]
