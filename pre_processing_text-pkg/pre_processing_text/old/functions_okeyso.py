import pandas as pd
import spacy
nlp = spacy.load('en_core_web_lg')
from collections import defaultdict        
from spacy.matcher import Matcher


# first transform to lemma, then drop stop words

def col_alpha_lemma(col):
    """
    Transform text into lemma without pronouns and spaces
    """
    # transform each DataFrame row into a nlp object
    nlp_col = nlp(col)
    # select a list of lemmas
    lemma_list = []
    for token in nlp_col:
        if token.pos_ != 'PRON' and token.pos_ !='SPACE' and token.is_alpha==True:
            lemma_list.append(token.lemma_.lower().strip())
    # return a string of elements
    return ' '.join(lemma_list)

def clean_sw(col):
    """
    Clean a list of symbols and stopwords
    """
    col = col_alpha_lemma(col)
    # transform each DataFrame row into a nlp object
    nlp_col = nlp(col)
    # select a list of lemmas
    clean_list = []
    for token in nlp_col:
        if token.is_stop==False:
            clean_list.append(token.text)
    return ' '.join(clean_list)

# DATAFRAME OF POS
def count_pos_col(col, pos_item):
    """
    count the number of pos in each tweet and return a dataframe
    """
    col_nlp = nlp(col)
    pos_list = []
    for token in col_nlp:
        if token.pos_ == pos_item:
            pos_list.append(token.pos_)
    return len(pos_list)

def df_count_pos(col, pos_item_list, df=False):
    """Iterate through a list of pos returning a 
    dataframe of their counts
    """
    # count the number of pos in each list element
    counts_pos = []
    for pos in pos_item_list:
#         print(pos)
        counts_pos.append(col.apply(count_pos_col, pos_item=pos))
    
    # transform the list into a dataframe
    df_pos = pd.DataFrame(counts_pos).T
    # rename the columns
    df_pos.columns = pos_item_list
    if df==False:
        return df_pos
    else:
        return pd.concat([df, df_pos], axis=1)
        

# return the length from each text
def len_text(col):
    return len(col)

# ENTITIES
def ent_from_col(col, ent_item):
    """
    Return a list of entities from a series
    """
    doc = nlp(col)
    # tuple with ent and ent label
    ent_text = [(ent, ent.label_) for ent in doc.ents]
    # returns entite that matches with the argument
    l_org = [word for word, ent in ent_text if ent==ent_item]
    # return a list of matched entities
    return l_org

def ent_list_to_df(col, list_ents_interest):
    """
    Enter a series and return a dataframe of entities
    """
    col_ent = []
    for ent in list_ents_interest:
        col_ent.append(col.apply(ent_from_col, ent_item=ent))
    ent_df = pd.DataFrame(col_ent).T
    ent_df.columns = [i.lower() for i in list_ents_interest]
    ent_df = ent_df.applymap(lambda x: ''.join(map(str, x)))
    return ent_df

def extract_ent(ent_text, ent_type=False):
    """
    Count the number of occurances and return a dictionary
    """
    d = defaultdict(int)
    for i in ent_text:
        d[i] +=1
    if ent_type==False:
        return d
    else:
        new_dict = defaultdict(int)
        for word, ent in d:
            if ent==ent_type:
                new_dict[word]+=1
        return new_dict

# MATCHER -- BETTER THAN REGULAR EXPRESSIONS

def col_matcher(col, pattern_name, pattern):
    # instantiate the nlp on each col
    doc = nlp(col)

    # instantiate the Matcher function
    matcher = Matcher(nlp.vocab)
    
    # add the pattern to the matcher
    matcher.add(pattern_name, None, pattern)

    # instantiate the matcher over the doc object
    matches = matcher(doc)
    
    # create a list of matches
    matcher_list = []
    for match_id, start, end in matches:
        # get the matcher span
        matcher_span = doc[start:end]
        # append the matcher_span within the list
        matcher_list.append(matcher_span)
    
    return str(matcher_list).replace('[', '').replace(']', '')