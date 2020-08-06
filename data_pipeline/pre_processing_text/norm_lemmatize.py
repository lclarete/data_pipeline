"""
NORMALIZATION

Lemmatization plays a huge part in normalizatio.
The process returns the word root based on the word's 
morphological classification, 
instead of just cutting the word -- 
like steaming. 

** spacy **
Favorite lib to lemmatize text is spacy.
It is charming: well documented, easy to use with 
tones of funcionalities.

https://spacy.io/usage
pip install -U spacy
pip install -U spacy-lookups-data
python -m spacy download en_core_web_sm


** textblob **
I've tested the function Word from textblob with 
the words 'running'. The returns was 'running'. 
Not even run. I've got bad results using it so far.

from textblob import Word
Word('running').lemmatize()


# Lemmatize Portuguese:
from nltk import PorterStemmer, RSLPStemmer

def portuguese_stemmer(string):
    porter = PorterStemmer()
    return [porter.stem(w) for w in word_tokenize(string)]


# http://snowball.tartarus.org/algorithms/portuguese/stemmer.html


"""

import spacy
from nltk.tokenize import word_tokenize


nlp_en = spacy.load('en_core_web_sm', disable=['tagger', 'parser', 'ner'])
nlp_pt = spacy.load('pt_core_news_sm', disable=['tagger', 'parser', 'ner'])

def lemmatize_string(string_text, nlp=nlp_en):
    """
    Iterate through each word in a string and lemmatize it.
    The process require a trained model, the variable nlp
    that loads a spacy model.
    
    Args:
        string_text: string of text
    Returns:
        string with lemmatized words
    """
    lemma = ''
    for token in nlp(string_text):
        
        # spacy replaces pronouns per -PRON-
        # in this case, if the word is a pronoun
        # returns the original text, not the lemma
        if token.lemma_ != '-PRON-':
            lemma += token.lemma_ + ' '
        else:
            lemma += token.text + ' '
            
    return lemma


def lemmatize_list(list_of_strings, nlp=nlp_en):
    """
    Apply the lemmatization function to a list of string texts.
    Input:
        list_of_strings: list of strings
        nlp: trained model
    
    Returns:
        list of strings with lemmatized words
    """

    return [lemmatize_string(w) for w in list_of_strings]





