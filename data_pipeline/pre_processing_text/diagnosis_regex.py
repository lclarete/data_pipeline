import pandas as pd

from data_pipeline.pre_processing_text.clean_list_regex import re_match_string
from data_pipeline.pre_processing_text.clean_list_regex import re_count_match_string
from data_pipeline.pre_processing_text.clean_list_regex import re_sub_match_string

from data_pipeline.pre_processing_text.clean_list_regex import func_re_list_strings, n_re_matches_list_strings


############################ --- Dictionary of regex --- ############################
from data_pipeline.pre_processing_text.clean_list_regex import list_to_df
from data_pipeline.pre_processing_text.clean_list_regex import n_re_matches_list_strings


def df_count_regex_matches(list_of_strings, dict_regex):
    """
    Returns a dataframe counting the number of regex matches.
    
    """
    list_of_regex_keys = list(dict_regex.keys())
    data = n_re_matches_list_strings(re_count_match_string, list_of_strings, dict_regex)
    
    return list_to_df(data, list_of_regex_keys)


useful_cols = ['hashtags', 'mentions', 'links', 'emails', 'emojis']

def df_matches(list_of_strings, dict_regex, useful_cols=useful_cols):
    """
    Args:
        list_of_strings: list of strings
        dict_regex: dictionary with regex
        useful_cols: only return those columns
    Returns a dataframe with the list of useful
    matches.

    Improvments: replace the name of the returned df
    from 'count_' to 'matched_'.
    """
    useful_cols = ['count_' + col for col in useful_cols]
    
    list_of_regex_keys = list(dict_regex.keys())
    data = n_re_matches_list_strings(re_match_string, list_of_strings, dict_regex)
    df = list_to_df(data, list_of_regex_keys)
    
    return df[useful_cols]



