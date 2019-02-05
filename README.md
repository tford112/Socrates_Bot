# Socrates_Bot

The simple socrates chat bot sources quotes stated by Socrates from here: https://www.keepinspiring.me/socrates-quotes/

socrates_quote.py -> scrapes the website for the relevant quotes and bio
bot.py -> Uses TF-IDF and Cosine Similarity to match user input with the most likely quote.

### TF-IDF
1. Term Frequency - Inverse Document Frequency is a method of relating how frequent a term is within a corpus
and then seeing how rare the occurrence is in the entire corpus. The latter is important to weed out common
words such as "man" from Socrates quotes as technically the word "man" will appear many times, but if it
appears everywhere then the value of the IDF will be low.

2. Cosine Similarity - measure of similarity between two non-zero vectors which is what we would get with a matrix of vectors of text represented by TF-IDF in vector space.
