"""
Count the frequency of words in a list 
by creating a dictionary of words as keys 
and counts as values.

There will be created a dictionary for each 
string in a list. Then, the dictionaries will 
be summed up into a single one.

"""

from collections import Counter
from functools import reduce
import operator

import numpy as np

from data_pipeline.pre_processing_text.split_ngrams import tokenize
from data_pipeline.pre_processing_text.preprocess_string_list import preprocessing_string


def count_words_list_of_strings(list_of_strings):
    """
    Returns a dict summing the number of words from each of a list os strings.
    Args:
        list_of_strings: list of docs as a string type
    """
    l = []
    # iterate through a list
    for string in list_of_strings:
        # tokenize each of the strings
        t = tokenize(string)
        # count the number of words
        count = Counter(t)
        # append the dictionaries into a list
        l.append(dict(count))
    
    # return the sum of all dictionaries
    return sum_dicts(l)


def sum_dicts(list_of_dicts):
    """
    Sum the elements from a list of dictionaries. 
    Support function to count_words_list_of_strings.
    Args:
        list_of_dicts: list of dictionaries with the frequency of each word
    """
    return dict(reduce(operator.add, map(Counter, list_of_dicts)))


def build_freqs(tweets, ys, list_of_regex, stopwords_list):
    """
    Build frequencies.
    Input:
        tweets: a list of tweets
        ys: an m x 1 array with the sentiment label of 
        each tweet (either 0 or 1)
    Output:
        freqs: a dictionary mapping each (word, sentiment) 
        part to its frequency.
    """

    # convert np array to list since zip needs an iterable
    # the squeeze is necessary or the list ends up with one element
    # this is just a NOP if ys is already a list
    yslist = np.squeeze(ys).tolist()

    # start with an empty dictionary and populate it 
    # by looping over all tweets and over all processed
    # words in each tweet.
    freqs = {}
    for y, tweet in zip(yslist, tweets):
        for word in preprocessing_string(tweet, list_of_regex, stopwords_list).split():
            pair = (word, y)
            if pair in freqs:
                freqs[pair] += 1
            else:
                freqs[pair] = 1
    return freqs

    ## also loop in a compact way
    # for y, tweet in zip(yslist, tweets):
    #     for word in process_tweet(tweet):
    #         pair = (word y)
    #         freqs[pair] = freqs.get(pair, 0) + 1




######## coursera function to process and count words ########
## https://uzpfirqi.coursera-apps.org/edit/utils.py

import re
import string
import numpy as np

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer


def process_tweet(tweet):
    """Process tweet function.
    Input:
        tweet: a string containing a tweet
    Output:
        tweets_clean: a list of words containing the processed tweet

    """
    stemmer = PorterStemmer()
    stopwords_english = stopwords.words('english')
    # remove stock market tickers like $GE
    tweet = re.sub(r'\$\w*', '', tweet)
    # remove old style retweet text "RT"
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    # remove hyperlinks
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
    # remove hashtags
    # only removing the hash # sign from the word
    tweet = re.sub(r'#', '', tweet)
    # tokenize tweets
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                               reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet)

    tweets_clean = []
    for word in tweet_tokens:
        if (word not in stopwords_english and  # remove stopwords
                word not in string.punctuation):  # remove punctuation
            # tweets_clean.append(word)
            stem_word = stemmer.stem(word)  # stemming word
            tweets_clean.append(stem_word)

    return tweets_clean


# how to create labels
# ys = np.append(np.ones((len(list_1))), np.zeros((len(list_2))))

def build_freqs_coursera(tweets, ys):
    """Build frequencies.
    Input:
        tweets: a list of tweets
        ys: an m x 1 array with the sentiment label of each tweet
            (either 0 or 1)
    Output:
        freqs: a dictionary mapping each (word, sentiment) pair to its
        frequency
    """
    # Convert np array to list since zip needs an iterable.
    # The squeeze is necessary or the list ends up with one element.
    # Also note that this is just a NOP if ys is already a list.
    yslist = np.squeeze(ys).tolist()

    # Start with an empty dictionary and populate it by looping over all tweets
    # and over all processed words in each tweet.
    freqs = {}
    for y, tweet in zip(yslist, tweets):
        for word in process_tweet(tweet):
            pair = (word, y)
            if pair in freqs:
                freqs[pair] += 1
            else:
                freqs[pair] = 1

    return freqs

