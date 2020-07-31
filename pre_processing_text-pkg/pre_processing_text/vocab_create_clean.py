"""
After cleaning the list of strings one by one,
the next step is create a vocab combining 
them all within a single string.

Functions that create and clean vocab.

* Vocab may be defined as a collection of texts.

In this case, to create a vocab, a list of strings
will be converted to a single string.

> ATTENTION <
The methods to clean the common and rare words 
from a vocab can is also coded to clean the same 
ones in a list of strings.
See the preprocessing_custom for more details.


"""

import pandas as pd
from functools import reduce
import operator
from pre_processing_text.dict_count_words import count_words_list_of_strings


def create_vocab(list_of_strings):
    """
    Aggregate a list of lists of strings into a single string
    
    Input: 
        list_of_strings: list of lists of strings
    Return:
        a string containing all the strings from the list_of_strings
    """
    
    list_to_string = ''

    for s in list_of_strings:
        list_to_string += s
    
    return list_to_string


#### clean vocab

def drop_rare_words(list_of_strings, n_count_words=2):
    """
    Exclude rare words.
    Agrs:
        d: dictionary counting words
        n_count_words: minimum number of frequency to consider
    Returns:
        String without words with a minium counts
    """
    d = count_words_list_of_strings(list_of_strings)
    
    return ' '.join([k for k, v in d.items() if v > n_count_words])


def drop_common_words(list_of_strings, n_top_words=20):
    """
    Returns a string without the n_top_words common words
    Args:
        list_of_strings: list of string
        n_top_words: number of most comon words to be excluded
    """
    # create a dictionary
    d = count_words_list_of_strings(list_of_strings)
    
    # 
    df = pd.DataFrame(data=d.items(), columns=['words', 'count']).sort_values(by='count', ascending=False)[n_top_words:]
    return ' '.join(df.words.to_list())
    


