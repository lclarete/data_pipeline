"""
Sandbox to test new functions.
Some were collected from past projects.

If useful, try to include them into the new pipeline.
"""


import pandas as pd


# 
def rename_cols(df):
    cols = df.columns
    cols = cols.str.replace(' ', '_').str.lower().str.replace('.', '_')
    df.columns = cols
    return(df)


# feature extracton
def emojis(col):
    pattern = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-\u26FF\u2700-\u27BF']"
    emoji = regexp_tokenize(col, pattern)
    return(emoji)


# FILE tweets_bolsonaro

# Ruled bases classification
# * Connect with Gspreadsheet available at: https://docs.google.com/spreadsheets/d/1QCoj40GLI9nvj8tTxuMROqLGJlu1QLd0E8w1mwE2cdw/edit#gid=0

from sys import path
path.append('/Users/liviaclarete/gdrive/code/functions/')

from GoogleSheet_read_returns_df import gsheet_returns_df
from GoogleSheet_writes_gsheet import write_df_gsheet
from NLP_count_themes_boolean import count_themes


# returns a boolean series after searched for a string pattern
def count_themes(col, df, pattern_df):
    # extrat list of lables
    subject_list = [i for i in pattern_df.iloc[:,0]]
    # extrat list of patterns
    pattern_list = [i for i in pattern_df.iloc[:,1]]
    pattern_extraction = []
    # interate through each pattern element
    for i in pattern_list:
        # for each pattern extract matched terms and returns a boolean
        pattern_extraction.append(df[col].str.extract((i)).notnull())
    # concat the list
    df_themes = pd.concat(pattern_extraction, axis=1)
    # rename new dataframe
    df_themes.columns = subject_list
    # concat the original with the new dataframe
    df_total = pd.concat([df, df_themes], axis=1)
    return(df_total, df_themes)


# retrieve stringlines from a google spreadsheet
# strings_df = gsheet_returns_df('tematicas_bolsonaro', 'strings_bolsonaro')

# df_total, df_themes = count_themes('text_clean', df, strings_df)

# table = pd.DataFrame([df_themes.sum()/df_themes.shape[0]*100, df_themes.sum()]).T
# table.columns = ['%', 'count']
# table = table.sort_values(by='count', ascending=False)

# calculate the total number of classified tweets
# returns a column summing the number of True's
# df_themes['total'] = df_themes.sum(axis=1)

# # transform the number into a boolean
# df_themes['total'] = df_themes.total.apply(lambda x: x>0)

# # sum the total number of True's in total column
# label_tweets = round(df_themes.total.sum()/df_themes.total.shape[0]*100)

# print(f'{label_tweets}% of tweets were classified. Still {100-label_tweets} to classified.')