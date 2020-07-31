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


from pre_processing_text.s_string_regex import re_sub_match_string

# does not workd importing from the root file
# from preprocessing_custom import re_sub_match_string

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


