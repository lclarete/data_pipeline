"""
Macgyver way to import all the files I need
even when I rename them -- which is 
constantly happen at this moment.

> ATTENTION IN THE ORDER TO IMPORT FUNCTIONS <
To work properly, the functions should be imported in
the same order they will be used. 
For instance,if a the function df_count_regex_matches 
needs s_string_regex as a dependancy, 
s_string_regex have to be imported first.

Next steps:
* Include optional arguments in a function.

"""

#### Necessary dependencies ####
import pandas as pd
import re
from collections import Counter

# from functools import reduce
# import operator

import spacy
# import unicode

from spellchecker import SpellChecker

### Cleaning support methods to build something useful ##
# string methods
from s_string_regex import re_count_match_string
from s_string_regex import re_match_string
from s_string_regex import re_sub_match_string

# methods to scale the string methods
from s_list_regex import func_re_list_strings
from s_list_regex import n_re_matches_list_strings

# format pandas
from s_list_format_pd import list_to_df

### ----------- VIEW / DIAGNOSIS  ----------- ###
from view_list_count_regex import df_count_regex_matches
from view_list_count_regex import df_matches

# from view_pos import xxx

### ----------- CLEANING LISTS ----------- ###

## List methods ##

### Clean rare and common words

from clean_list_regex import sub_several_regex_one_string
from clean_list_regex import sub_list_strings_list_regex, sub_several_regex_one_string

from clean_list_rare_common import drop_rare_words
from clean_list_rare_common import drop_common_words


### Drop stopwords
from clean_list_stopwords import remove_stopwords_string, remove_stopwords_list


### ----------- NORMALIZE LISTS ----------- ###

### Lemmatize lists
from norm_lemmatize import lemmatize_list, lemmatize_string


### strip accents
## Problem: no module named 'unicode'
## tried pip install Unidecode -- and nothing
# from norm_drop_accents import strip_accent

# from norm_spellchecker import NEED_TO_BUILD_FUNC


### ----------- LIST SPLITS: n-grams -----------  ###
from split_ngrams import tokenize

### Count dict ###
from dict_count_words import count_words_list_of_strings, sum_dicts
from dict_count_words import sum_dicts


### VOCAB METHODS ###

from vocab_create_clean import create_vocab
from vocab_create_clean import drop_rare_words
from vocab_create_clean import drop_common_words


# how to include a argument
def preprocessing_list(list_of_strings, list_of_regex, stopwords_list):
    """
    Apply the preprocessing functions to clean
    and normalize a list of string.

    Input:
        list_of_strings
    
    Output:
        list of strings cleaned and normalized
    """
    # clean regex patterns
    l = sub_list_strings_list_regex(list_of_strings, list_of_regex)
    # lemmatize words
    l = lemmatize_list(l)
    # drop stopwords -- for now, using the default sw list
    # I found online
    # Include sw as an optional argument
    return remove_stopwords_list(l)


"""
preprocessing_string, used for pandas columns, is not working properly.
Cases are not lower, also returning numbers and symbols
"""


def preprocessing_string(string_text, list_of_regex, stopwords_list):
    """
    Apply the preprocessing functions to clean
    and normalize a list of string.

    Input:
        list_of_strings
    
    Output:
        list of strings cleaned and normalized
    """
    # clean the regex patterns
    s = sub_several_regex_one_string(string_text, list_of_regex)

    # lemmatize string
    s = lemmatize_string(string_text)

    # drop stopwords
    return remove_stopwords_string(s)