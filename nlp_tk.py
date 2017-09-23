import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import chat


sentence = "What is the weather in Chicago?"
tokens = word_tokenize(sentence)

stop_words = set(stopwords.words('english'))

clean_tokens = [w for w in tokens if not w in stop_words]
tagged = nltk.pos_tag(clean_tokens)

c=nltk.ne_chunk(tagged)

print c
