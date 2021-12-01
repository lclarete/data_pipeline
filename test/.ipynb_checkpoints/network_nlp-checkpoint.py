"""
Entity recognition and build a netword with words
Based on a tutorial of NLP applied for SEO:

Colab code: https://colab.research.google.com/github/hamletbatista/sej/blob/master/An_Introduction_to_Natural_Language_Processing_with_Python_for_SEOs.ipynb
Tutorial: https://www.searchenginejournal.com/natural-language-processing-python-seo/377051/amp/
"""

import spacy
from spacy.matcher import Matcher

# instantiate the spacy model
nlp = spacy.load('en_core_web_sm')


import pandas as pd

import networkx as nx
import matplotlib.pyplot as plt


#####


# join a string
def nlt_text(list_of_strings, nlp=nlp):
    """
    Transform a list of strings into a single string,
    and transform it into a spacy object
    Input:
        list_of_strings: list of texts
        nlp: spacy object
    Output:
        spacy object

    To visualize the results in your Jupyter Notebook:
    displacy.render(doc, style='ent', jupyter=True)
    """
    # transform the list of strings into a single string
    text = '\n'.join([x for x in list_of_strings if x > 0])
    # return the nlp object
    return nlp(text)

######################## RELATIONSHIP STRING ########################
def get_relation(string, nlp=nlp):
    """
    Returns a list of unigrams and bi-grams,
    using the class Matcher from spacy
    Input:
        list_of_strings
        nlp
    Output:
        list of expressiosn
    """

    doc = nlp(string)

    # Matcher class object 
    matcher = Matcher(nlp.vocab)

    #define the pattern 
    pattern = [{'DEP':'ROOT'}, 
            {'DEP':'prep','OP':"?"},
            {'DEP':'agent','OP':"?"},  
            {'POS':'ADJ','OP':"?"}] 

    matcher.add("matching_1", None, pattern) 

    matches = matcher(doc)
    k = len(matches) - 1

    span = doc[matches[k][1]:matches[k][2]] 

    return(span.text)

######################## RELATIONSHIP LIST ########################

def get_relation_list(list_of_strings):
    """
    Input:
        list_of_strings: text
    Output:
        list of relationships
    """
    relations_list = []

    for string in list_of_strings:
        if len(string) > 0:
            relations_list.append(get_relation(string))

    return relations_list


######################## ENTITIES STRING ########################

def get_entities(string):
    ## chunk 1
    ent1 = ""
    ent2 = ""

    prv_tok_dep = ""    # dependency tag of previous token in the sentence
    prv_tok_text = ""   # previous token in the sentence

    prefix = ""
    modifier = ""

    #############################################################

    for tok in nlp(string):
        ## chunk 2
        # if token is a punctuation mark then move on to the next token
        if tok.dep_ != "punct":
          # check: token is a compound word or not
            if tok.dep_ == "compound":
                prefix = tok.text
            # if the previous word was also a 'compound' then add the current word to it
                if prv_tok_dep == "compound":
                    prefix = prv_tok_text + " "+ tok.text

          # check: token is a modifier or not
        if tok.dep_.endswith("mod") == True:
            modifier = tok.text
            # if the previous word was also a 'compound' then add the current word to it
            if prv_tok_dep == "compound":
                modifier = prv_tok_text + " "+ tok.text

          ## chunk 3
        if tok.dep_.find("subj") == True:
            ent1 = modifier +" "+ prefix + " "+ tok.text
            prefix = ""
            modifier = ""
            prv_tok_dep = ""
            prv_tok_text = ""      

          ## chunk 4
        if tok.dep_.find("obj") == True:
            ent2 = modifier +" "+ prefix +" "+ tok.text

      ## chunk 5  
      # update variables
        prv_tok_dep = tok.dep_
        prv_tok_text = tok.text
    #############################################################

    return [ent1.strip(), ent2.strip()]


######################## ENTITIES LIST ########################

def get_entities_list(list_of_strings):
    """
    Input:
        list_of_strings: text
    Output:
        list of relationships
    """
    entity_pairs = []

    for string in list_of_strings:
        if len(string) > 0:
            entity_pairs.append(get_entities(string))

    return entity_pairs

######################## PRINT THE GRAPH ########################

def df_entity_pairs(entity_pairs, relations):
    """
    Create a dataframe with the entity_pairs
    Input:
        entity_pairs: get it using the function get_entities_list
        relations: get it using the function get_relation_list
    Output:
        dataframe
    """
    
    # extract subject
    source = [i[0] for i in entity_pairs]

    # extract object
    target = [i[1] for i in entity_pairs]

    df = pd.DataFrame({'source':source, 'target':target, 'edge':relations})
    
    return df



def display_graph(relation, entity_pairs, relations_list, total_chart=False):
    """
    Print a network chart.
    Input:
        relation: word that will retrieve only this specific relationship
        entity_pairs: pairs of entities
        relations_list: relations list
    Output:
        network chart

    get_entities_list(list_of_strings)
    """

    # create a dataframe with the entity_pairs
    # entity_pairs: pair of words. 
    # This input could be generated using the 
    # function get_entities_list(list_of_strings)
    kg_df = df_entity_pairs(entity_pairs, relations_list)

    # plot the total chart
    # don't to it, the output is a total mess
    if total_chart==True:
        G=nx.from_pandas_edgelist(kg_df, "source", "target", edge_attr=True, create_using=nx.MultiDiGraph())

    else:

        G=nx.from_pandas_edgelist(kg_df[kg_df['edge']==relation], "source", "target", edge_attr=True, create_using=nx.MultiDiGraph())

    plt.figure(figsize=(12,12))

    pos = nx.spring_layout(G, k = 0.5) # k regulates the distance between nodes

    nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_cmap=plt.cm.Blues, pos = pos)

    plt.show()