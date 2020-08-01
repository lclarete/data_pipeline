"""
Paying more attention to the unites I'll be using
for processing data.

The most common used is tokenization.
We can also use bi-grams, tri-grams or n-grams.

This is the space to learn and test them.

"""


def tokenize(string_text):
    """
    Split a string based on the space between words
    Input:
        string_text: text type string
    Output:
        list of words splitted by space
    """
    return string_text.split()


def tokenize_list(list_of_strings):
    """
    Tokenize a list of strings
    Input:
        list_of_strings
    Output:
        list of lists with tokenized words
    """
    return [tokenize(string) for string in list_of_strings]


# # build-in functions
# from nltk.tokenize import word_tokenize, TweetTokenizer
# from nltk.collocations import *

# import nltk
# # words_bigam = nltk.collocations.BigramAssocMeasures()

# # words_finder = nltk.BigramCollocationFinder.from_words(clean_text)



# ### Using spacy to tokenize

# import pandas as pd

# import spacy
# from spacy.tokenizer import Tokenizer
# from spacy.lang.en import English
# from spacy import displacy

# from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# from sklearn.base import TransformerMixin
# from sklearn.pipeline import Pipeline

# from sklearn.model_selection import train_test_split

# # clean stopwords, numbers, punctuation and return the token's lemma
# def spacy_tokenizer(sentence, tokenizer=True):
#     # creating token objects
#     tokens = nlp(sentence)
#     tokens_list = []
#     for t in tokens:
#         # clean punctuation and stopwords
#         if t.is_alpha == True and t.is_stop == False:
#             tokens_list.append(t.lemma_.lower().strip())
#     if tokenizer==False:
#         return ' '.join(tokens_list)
#     else:
#         return tokens_list

# spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
# stop_words = spacy.lang.en.stop_words.STOP_WORDS
# punctuations = string.punctuation


# def spacy_tokenizer(sentence):
#     # Creating our token object, which is used to create documents with linguistic annotations.
#     mytokens = nlp(sentence)

#     # Lemmatizing each token and converting each token into lowercase
#     mytokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]

#     # Removing stop words
#     mytokens = [ word for word in mytokens if word not in stop_words and word not in punctuations ]

#     # return preprocessed list of tokens
#     return mytokens

    