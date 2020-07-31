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

from pre_processing_text.split_ngrams import tokenize


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