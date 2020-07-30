import pandas as pd

# returns a boolean series after searched for a string pattern
def count_themes(col, df, pattern_df):
    # extrat list of lables
    columns_list = [i for i in pattern_df.iloc[:,0]]
    # extrat list of patterns
    pattern_list = [i for i in pattern_df.iloc[:,1]]
    pattern_extraction = []
    # interate through each pattern element
    for i in pattern_list:
        # for each pattern extract matched terms and returns a boolean
        pattern_extraction.append(df[col].str.extract(i).notnull())
    # concat the list
    df_themes = pd.concat(pattern_extraction, axis=1)
    # rename new dataframe
    df_themes.columns = columns_list
    # concat the original with the new dataframe
    df_total = pd.concat([df, df_themes], axis=1)
    return(df_total, df_themes)