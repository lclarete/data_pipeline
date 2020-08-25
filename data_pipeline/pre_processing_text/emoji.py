"""
Working with emojis: https://emojipedia.org/

Using the package advertools to get emojis from text
https://advertools.readthedocs.io/en/master/advertools.emoji.html
"""


import advertools as ad
import pandas as pd

def counting_emojis(list_of_strings, type_of_emoji='top_emoji_text', overview=False):
    """
    Count the number of each emoji in a string 
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
            
            ## >> list of emoji's categories:
            ## >> emojis_categ = ['top_emoji_text', 'top_emoji', 'top_emoji_groups', 'top_emoji_sub_groups']
                
    Output:
        dataframe counting the number of each emoji
            from the vocab
        If the 'overview' parameter is equal True,
            return a dataframe with metrics per post
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
    


## apply the function above to retrieve dataframes
## from emojis, images, sub_categs and categs

def retrieving_categ_emojis(list_of_strings):
    """
    Apply the counting_emojis function to retrieve 
    the emoji classes, and subclasses
    Input:
        list_of_strings: string or list of strings
    Output:
        dataframe with three colums: emoji, n, and type
    """
    # list of categories
    emojis_categ = ['top_emoji_text', 'top_emoji', 'top_emoji_groups', 'top_emoji_sub_groups']
    
    # create a dataframe
    dfs = pd.DataFrame()
    
    # iterate over the categories 
    for categ in emojis_categ:
        # apply the function to count the number of emojis
        emoji_dfs = return_df_count_emojis(df.tweet_full_text, 
                                           type_of_emoji=categ,
                                           overview=False)
        # create a new column to describe the information retrieved
        emoji_dfs['type'] = categ
        # concat the datasets
        dfs = pd.concat([dfs, emoji_dfs], axis=0)

    # return the concated dataset    
    return dfs
    