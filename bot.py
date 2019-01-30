from socrates_quotes import read
import nltk
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import pandas as pd


## there is a new line character added so as to read in the values easier for tfidf
quotes = read("soc_q.csv")


## Greetings
greet_input = ["Hi", "How are you doing", "What's up", "Howdy"]
greet_output = ["Hello", "Greetings", "You seek answers"]

def greet(input):
    for word in input.split():
        if word.lower() in greet_input:
             return random.choice(greet_output)

def response(user_input):
    robo = ""
    quotes.append(user_input)
    tfidf_vec = TfidfVectorizer(stop_words = "english")
    tfidf = tfidf_vec.fit_transform(quotes)
    vals = cosine_similarity(tfidf[-1], tfidf[:-1])
    ## argsort returns an ordered list of cos_sim and indices
    idx = vals.argsort()[0][-1]  ## need the last elem index which is the highest cos_simi

    ## cosine_similarity will return similarity values. If all are 0 then no dice
    if np.all(vals == 0):
        robo += "That is beyond the realm of my limited knowledge..."
        return robo
    else:
        robo += quotes[idx]
        return robo

def chat():
    user_input = input()
    print(greet(user_input))
    print("What is your question?")
    user_question = input()
    r = response(user_question)
    print(r)

chat()
