'''Insert some documentation'''


import pandas as pd

# AVERAGE WORD LENGHT
def avg_word(row):
    words = row.split()
    word_lenght = [len(i) for i in words]
    avg_word = sum(word_lenght)/len(word_lenght)
    return(avg_word)

def feature_extraction_words(col, df):
    # COUNT WORDS OF EACH TWEET
    # iterate through each row with apply, iterate through each word with lambda
    word_count = col.apply(lambda x: len(str(x).split(' ')))
    # COUNT CHARACTERS 
    char_count = col.str.len()
    # AVERAGE WORD LENGHT
    word_lenght = col.apply(lambda x: (avg_word(x)))
    # concat the three new cols
    df_new = pd.concat([word_count, char_count, word_lenght], axis=1)
    # rename columns
    df_new.columns = ['word_count', 'char_count', 'avg_word_lenght']
    # concat new df with the original one
    df_new = pd.concat([df, df_new], axis=1)
    return(df_new)






