"""
This file has a set of 8 functions: 3 of them match, 
count or replace a string pattern within a single string.

They are the the building blocks for other functions 
to handle the same task with a set of regex,
in a list of strings.

Settle to used as an argument in the function
func_re_list_strings()

--- 
The other 4 functions scales the same task of matching,
counting and replacing from a string to a list of strings.

It presents a single function that receives 
the previous 3 functions as arguments.

The last one formats a dataframe.

"""

import re
import pandas as pd


# --------- string + one regex --------- #


def re_match_string(string_text, regex):
    """
    Matches and extract a regex pattern within a string.
    Args:
        string_text: text format that will be searched
        regex: regular expression pattern to be searched
    Returns a list with extracted patterns.
    """
    return re.findall(regex, string_text)


def re_count_match_string(string_text, regex):
    """
    Count the number of matched patterns in a string.
    Args:
        string_text: text format that will be searched
        regex: regular expression pattern to be searched
    Returns an integer counting the numbers of matches.
    """
    return len(re_match_string(string_text, regex))


def re_sub_match_string(string_text, regex):
    """
    Matches and replace a regular expression pattern within a list.
    Args:
        string_text: text format that will be searched
        regex: regular expression pattern to be searched
    Returns a lower case cleaned string
    """
    # regex = re.compile(regex)
    # return regex.sub('', string_text.lower()).strip()
    
    sub_string = re.sub(regex, '', string_text.lower()).strip()
    return ' '.join([w for w in sub_string.split()])


# --------- list of strings (n strings) + regex  --------- #



def func_re_list_strings(func, list_of_strings, regex):
    """
    Iterate over each list's string and apply a function
    in each one of them.

    Args:
        list_of_strings: list of strings
        regex: regular expression pattern
        func: re_match_string, re_count_match_string or 
              re_sub_match_string

    Returns a list of elements:
        re_match_string: list of matches
        re_count_match_string: number of matches
        re_sub_match_string: string without the match
    """
    return [func(s, regex) for s in list_of_strings]


# --------- list of strings (n strings) + list of regex (n regex) --------- #

"""
Scale: apply the func_re_list_strings to a list regex patterns
"""


def n_re_matches_list_strings(func, list_of_strings, dict_regex):
    """
    Iterate through a list of regex, use it as argument for the function
    Args:
        list_of_strings: list of strings
        dict_regex: dictionary with key as the regex description and values as the regex pattern

    Returns a list of lists with elements:
        re_match_string: list of matches
        re_count_match_string: number of matches
        *****
        Weird results for re_sub_match_string. 
        
    """
    # returns a list counting the number of matches for each regex
    return [func_re_list_strings(func, list_of_strings, regex=regex) for regex in list(dict_regex.values())]

"""
Clean a list of strings using a list of 
regular expressions. 
If the regex are stored in a dictionary, 
use the method .values() to retrive the 
regex list.
Eg.
d = {'description_p1': 'regex-pattern1'}
list_of_regex = list(d.values())
"""


def sub_several_regex_one_string(string_text, list_of_regex):
    """
    Iterates over a list of regex, dropping them from a single string.
    
    Args:
        list_of_strings: list of strings
        list_of_regex: list of regex patterns
        
    Returns a single cleaned string
    """
    for regex in list_of_regex:
        string_text = re_sub_match_string(string_text, regex)
    
    return string_text
    

def sub_list_strings_list_regex(list_of_strings, list_of_regex):
    """
    Replace a list of regex patterns over a list of strings
    
    Args:
        list_of_strings: list of strings
        list_of_regex: list of regex patterns

    Returns a list of cleaned strings.
    """
    return [sub_several_regex_one_string(string, list_of_regex) for string in list_of_strings]


"""
Include functions to format a dataframe.

"""


def list_to_df(list_of_outputs, list_of_regex_keys):
    """
    Receives a list and transform it into a formated dataframe
    
    """
    # create a data frame with the list of counts and transpose it
    df = pd.DataFrame(data=list_of_outputs).T

    # set the columns as the keys from the dict_regex
    df.columns = list_of_regex_keys
    df = df.add_prefix('count_')
    
    return df