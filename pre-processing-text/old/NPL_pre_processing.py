# removing stopwords
from sys import path
path.append('/Users/liviaclarete/gdrive/code/functions/')
from GoogleSheet_stopwords import stop_words_gsheet

from nltk.corpus import stopwords


# tokenize words from the text
def split_words_col(col):
    serie = pd.Series(col.apply(lambda x:x.split()))
    return(serie)



'''# Lemmatization
Lemmatization returns the root word based on the word's 
morphological classification, instead of just excluding
the word sufficies like steaming. Lemmatization is more
 effective and preferable rather than stemming.'''

from textblob import Word
def lemmatize_col(col):
    col = col.apply(lambda x: ' '.join(
        [Word(x).lemmatize() for x in x.split()]))
    return(col)

def pre_processing_col(col):
    # transform the words into lower case
    col = col.apply(lambda x: x.lower())
    # removing punctuation
    col = col.str.replace('[^\w\s]', '')
    # removing numbers
    col = col.apply(
    # iterate through each item in a returns a list of words and joins the split words into a sentence again
    lambda x:' '.join([x for x in x.split() if not x.isdigit()]))
    # stopwords
    stopwords = stop_words_gsheet()
    # removing stopwords
    col = col.apply(lambda x: ' '.join([x for x in x.split() if x not in stopwords]))
    return(col)
