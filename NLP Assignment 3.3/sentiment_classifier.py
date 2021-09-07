import pickle
import re
import pandas as pd
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
lemmatizer = WordNetLemmatizer()

model = pickle.load(open('model', 'rb'))
vectorizer = pickle.load(open('vectorizer', 'rb'))

def get_wordnet_pos(pos_tag):
    if pos_tag.startswith('J'):
        return wordnet.ADJ
    elif pos_tag.startswith('V'):
        return wordnet.VERB
    elif pos_tag.startswith('N'):
        return wordnet.NOUN
    elif pos_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def text_cleaner(X):
    corpus = []
    for i in X:
        review = re.sub(r'\W', ' ', i)
        review = review.lower()
        review = re.sub(r'^br$', ' ', review)
        review = re.sub(r'\s+br\s+',' ',review)
        review = re.sub(r'\s+[a-z]\s+', ' ',review)
        review = re.sub(r'^b\s+', '', review)
        review = re.sub(r'\s+', ' ', review)
        corpus.append(review)
    return X

def sentiment(review):
    sample = [text_cleaner(review)]
    pos_tags = pos_tag(sample)
    sample = [WordNetLemmatizer().lemmatize(text[0], get_wordnet_pos(text[1])) for text in pos_tags]
    sample = vectorizer.transform(sample).toarray()
    sentiment = model.predict(sample)
    confidence = max(model.predict_proba(sample)[0])

    if sentiment[0] == 2:
        return ("Positive", confidence)
    elif sentiment[0] ==1:
        return ("Neutral", confidence)
    else:
        return ("Negative",confidence)


while True:
    text = input("Please input your review: ")
    print("Your review sentiment is: ",sentiment(text)[0],"\nConfidence percentage: ", sentiment(text)[1])
    print("___________________")
