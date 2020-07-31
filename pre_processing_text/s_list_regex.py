################## --- VOCAB FUNCTIONS > RECEIVES A LIST --- ##################

# --------- list of strings (n strings) + regex  --------- #

"""
Applystring functions to a list of strings.

It presents a single function that receives 
the previous 3 functions as arguments.

Scale from a string to a list of strings.
"""

from s_string_regex import re_match_string
from s_string_regex import re_count_match_string
from s_string_regex import re_sub_match_string



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