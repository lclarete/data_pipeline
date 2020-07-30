"""
This is an attempt to rebuild a simpler preprocessing
pipeline.

This pipeline can clean spaces, punctuation, digits,
and stopwords, returning the lemma at the end.

Missing cleaning process:
* remove links, hashtags and mentions

Temptive 1: do not remove symbols and emojis
Temptive 2: remove symbols and emojis


Before applying the following functions,

Download the trained bases for each language:
! python -m spacy download en_core_web_sm
! python -m spacy download en_core_web_md
! python -m spacy download en_core_web_lg

# Faster running processing if disabling some elements
from a pipeline
https://spacy.io/usage/processing-pipelines#disabling


Source:
https://github.com/explosion/spaCy/issues/1837
https://medium.com/better-programming/extract-keywords-using-spacy-in-python-4a8415478fbf

"""

from collections import Counter
from string import punctuation

import spacy

disable_pipe = ['parser', 'ner']

nlp = spacy.load('en_core_web_lg', disable=disable_pipe)
# nlp = spacy.load('en_core_web_sm')
nlp.pipe_names


#################### --- attemptive 1 --- ####################

def get_hotwords(string_text):
    """
    Clean stopwords, and punctuation,
    return proper noun, adjective and noun
    
    Input:
        string_text: string of text
    
    Output:
        cleaned string text
    """

    result = []

    # set part of speech that will be selected
    pos_tag = ['PROPN', 'ADJ', 'NOUN']

    # normalize: convert the input string into lower case
    doc = nlp(string_text.lower())

    # loop over each of the tokens 
    for token in doc:

        # check if the token is a stop word or is a punctuation
        if (token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        
        # keep the token if it is part of post_tag categories
        if (token.pos_ in pos_tag):
            # append the token into a list
            result.append(token.text)
    
    # return a string of cleaned tokens
    return ' '.join(result)


def get_hotwords_list(list_of_strings):
    """
    Apply the get_hotwords function in a list of strings
    
    Input:
        list_of_strings
        
    Output:
        list of cleaned strings
    """
    return [get_hotwords(string) for string in list_of_strings]


#################### --- attemptive 2 --- ####################

def token_filter(token, len_word=4):
    """
    Use spacy to filter punctuation, spaces, stopwords 
    and words with less than 3 characters.
    Replace regular expressions clean and stopwords removal
    Input:
        token: tokenized word
        len_word: minimun length of a word

    Output:
        cleaned token
    """
    return not (token.is_punct | token.is_space | token.is_stop | token.is_digit | len(token) <= len_word)


def spacy_tokenizer_string(string_text):
    """
    Returns the word lemma and drop punctuation spaces, 
    stowords and words with less than n characters
    
    Input:
        string_text
        
    Output:
        string cleaned
    """
    for doc in nlp.pipe([string_text.lower()]):
        tokens = [token.lemma_ for token in doc if token_filter(token)]
    return ' '.join(tokens)

def spacy_tokenize_list(list_of_strings):
    """
    Apply the spacy_tokenizer_string function into 
    every single string of a list of strings

    Input:
        list_of_strings

    Output:
        list of cleaned strings
    """
    return [spacy_tokenizer_string(string) for string in list_of_strings]
