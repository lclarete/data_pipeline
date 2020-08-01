"""
Exclude the rare and most frequent words and return a string/ list of strings.
The idea is to count the total words from the vocab,
then count the words from it.
After having the counts, drop each common/ rare word from each string
Return the original string without each common/ rare word
"""


import pandas as pd
from data_pipeline.pre_processing_text.dict_count_words import count_words_list_of_strings


def drop_rare_words(list_of_strings, n_count_words=2):
    """
    Exclude rare words.
    Agrs:
        d: dictionary counting words
        n_count_words: minimum number of frequency to consider
    Returns:
        String without words with the words that haven't reached the
        minimun frequence -- callsed rare words
    """
    d = count_words_list_of_strings(list_of_strings)
    
    return ' '.join([k for k, v in d.items() if v > n_count_words])


### work on it -- returning empty string
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
    
