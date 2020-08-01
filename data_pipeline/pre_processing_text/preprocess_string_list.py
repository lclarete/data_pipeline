"""
Process strings and list of strings.
"""


from data_pipeline.pre_processing_text.clean_list_regex import sub_list_strings_list_regex, sub_several_regex_one_string

from data_pipeline.pre_processing_text.norm_lemmatize import lemmatize_list, lemmatize_string

from data_pipeline.pre_processing_text.clean_list_stopwords import remove_stopwords_string, remove_stopwords_list


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