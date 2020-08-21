"""
Working with emojis: https://emojipedia.org/

Using the package advertools to get emojis from text
https://advertools.readthedocs.io/en/master/advertools.emoji.html
"""


import advertools as ad
import pandas as pd

def return_df_count_emojis(list_of_strings, type_of_emoji='top_emoji_text', overview=True):
    """
    Count the number of each emoji within a string 
    or a list of strings
    Input:
        list_of_strings: string or list of strings
        type_of_emoji: individual emojis or categories. 
            Possible parameters:
            # individual emojis
                default: top_emoji_text: emoji discription
                top_emoji: emoji images and the number of posts with the emoji
            # categories
                top_emoji_groups: description of emoji groups
                top_emoji_sub_groups: description of emoji subgroups
                
    Output:
        dataframe counting the number of each emoji
        from the vocab
    """
    # extract the emojis
    emoji_summary = ad.extract_emoji(list_of_strings)[type_of_emoji]
    # create a dataframe with the returned dictionary
    df = pd.DataFrame(emoji_summary)
    # rename the columns
    df.columns = ['emoji', 'n']
    
    # return overview
    if overview==True:
        metrics_post = ad.extract_emoji(list_of_strings)['overview']
        df_metrics_post = pd.DataFrame(list(metrics_post.items()))
        df_metrics_post.columns = ['description', 'metric']
    
        return df, df_metrics_post
    
    else:
        return df
    