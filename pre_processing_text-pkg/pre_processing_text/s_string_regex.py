"""
This file has a set of 3 functions that match, count 
or replace a string pattern within a single string.

This is the building blocks for other functions 
to handle the same task with a set of regex,
in a list of strings.

Settle to used as an argument in the function
func_re_list_strings()

"""


import re


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
