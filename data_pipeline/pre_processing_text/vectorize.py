"""
Vectorize: to infer the latent structure in our corups 
we need a way to represent documents that we can
manipulate mathematically.

dense vector: explicit answers to specific questions


sparse vector or bag-of-words vector

Source: https://radimrehurek.com/gensim/auto_examples/core/run_core_concepts.html


Gesim:
* word2vec: train to find word vectors and then 
run similarity queries between words.

* doc2vec: tag text and get tag vectors.
https://stackoverflow.com/questions/42827175/gensim-what-is-difference-between-word2vec-and-doc2vec#:~:text=1%20Answer&text=In%20word2vec%2C%20you%20train%20to,authors%20as%20tags%20on%20documents.

* doc2bow:

"""

import gensim
from gensim import corpora
from gensim import models

from data_pipeline.pre_processing_text.split_ngrams import tokenize_list


def bow_corpora(list_of_strings, tfidf=False):
    """
    Vectorize list of strings
    Input:
        list_of_strings

    Output:
        vector
    """

    # tokenize list
    token_list = tokenize_list(list_of_strings)

    # creating a term dictionary with the corpus
    dictionary = corpora.Dictionary(token_list)

    # creating a Document Text Matrix with the dictionary
    # also called bow_corpus
    doc_term_matrix = [dictionary.doc2bow(i) for i in token_list]
    
    if tfidf==False:
        return doc_term_matrix

    if tfidf==True:
        tfidf = models.TfidfModel(doc_term_matrix)
        return tfidf[dictionary.doc2bow(token_list)]



def lda_topic_modeling(list_of_strings):

    dictionary, doc_term_matrix = doc2bow_vectorize(list_of_strings)
    
    # Creating the object for LDA model using gensim library
    LDA = gensim.models.ldamodel.LdaModel

    # Build LDA model
    lda_model = LDA(corpus=doc_term_matrix,
                    id2word=dictionary,
                    num_topics=7, 
                    random_state=100,
                    chunksize=1000,
                    passes=50)
    
    print(lda_model.print_topics(), '\n\n')
    
    print('--------------------------------')
    instruction = 'Visualizing the model: import pyLDAvis; pyLDAvis.enable_notebook(); vis = pyLDAvis.gensim.prepare(lda_model, doc_term_matrix, dictionary); vis'
    
    print(instruction)
    
    return lda_model, doc_term_matrix, dictionary