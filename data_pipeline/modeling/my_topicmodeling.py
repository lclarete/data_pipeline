"""
Implement topic modeling.
First draft.

Learn how to interpret the results from topic modeling.
What is:
* topic_coordinates
* topic_info
* cluster
* token_table and the weights related to each one
* relevance λ
* marginal topic distribution
* Intertopic Distancce Map (via multidimensional scaling)
* What is the metric to rank the most salient terms?
* loglift
* logprob
* R
* lambda_step
* plot_opts={'xlab': 'PC1', 'ylab': 'PC2'}

- Describe the process and algoritm used
- Include sources

https://shichaoji.com/tag/topic-modeling-python-lda-visualization-gensim-pyldavis-nltk/
https://github.com/bmabey/pyLDAvis/blob/master/notebooks/GraphLab.ipynb
https://github.com/bmabey/pyLDAvis/blob/master/notebooks/pyLDAvis_overview.ipynb

https://github.com/bmabey/pyLDAvis


"""

import gensim
from gensim import corpora
import pyLDAvis
import pyLDAvis.gensim
import matplotlib.pyplot as plt
import seaborn as sns

from data_pipeline.pre_processing_text.split_ngrams import tokenize_list


def lda_topic_model(list_of_strings):
    """
    Apply LDA model to a list of strings
    Input:
        list_of_strings

    Output:
        list of related topics
    """

    token_list = tokenize_list(list_of_strings)

    # creating a term dictionary with the corpus
    # receivees a list of lists with tokenized strings
    dictionary = corpora.Dictionary(token_list)

    # creating a Document Text Matrix with the dictionary
    doc_term_matrix = [dictionary.doc2bow(i) for i in token_list]

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