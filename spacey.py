import spacy
import re
import io
from collections import Counter
spacy.prefer_gpu()
nlp = spacy.load("en_core_web_sm")

# change file according to what you text file you want to process
with open('D2.txt', encoding='utf-8') as tweets:
    text = tweets.read()
#adds lower case so that words are not miscounted.
text = text.lower()

#open the file you wish to write to.
file = io.open("CommonWords_covid-count.txt", 'a+', encoding='utf-8')

doc = nlp(text)

# counts unique tokens and filters out garbage values that cannot be processed
# properly
words = [token.text for token in doc if not token.is_stop and not
 token.is_punct and not token.text.isspace() and not token.text == "&amp"
 and not token.text =="amp"]
# five most common tokens
word_freq = Counter(words)
common_words = word_freq.most_common(100)

# print(common_words)  #flag
unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
# print (unique_words)  #flag

y = len(unique_words)
# print(words)   #flag
print(y)
# print(common_words)   #flag

# write to file
for x in range(len(common_words)):
    file.write(str(common_words[x][1]))
    file.write("\n")
