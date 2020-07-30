"""
Include functions to format a dataframe.

"""

import pandas as pd

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