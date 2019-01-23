from socrates_quotes import read
import nltk
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import pandas as pd


quotes = read("soc_q.csv")

## Greetings
greet_input = ["Hi", "How are you doing", "What's up", "Howdy"]
greet_output = ["Hello", "Greetings", "You seek answers"]

def greet(input):
    for word in input.split():
        if word.lower() in greet_input:
            return random.choice(greet_output)


def response(user):
    robo = ""
    quotes.append(user)
    tfidf_vec = TfidfVectorizer(stop_words = "english")
    tfidf = tfidf_vec.fit_transform(quotes)
    vals = cosine_similarity(tfidf[-1], tfidf[:-1])
    idx = vals.argsort()[0]
    vals.sort()
    ## cosine_similarity will return 2 values. If both are 0 then no dice
    if np.all(vals == 0):
        robo += "That is beyond the realm of my limited knowledge..."
        return robo
    else:
        # robo = quotes[idx]
        print(robo)
    # print(pd.DataFrame(tfidf.toarray(),columns=tfidf_vec.get_feature_names()))
    print(vals)

response("love")
