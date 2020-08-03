"""
Class and functions to perform topic modeling.

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

Topic Modeling with LSA, PLSA, LDA & lda2Vec:
https://medium.com/nanonets/topic-modeling-with-lsa-psla-lda-and-lda2vec-555ff65b0b05

Topic modeling with NMF and SVD:
http://localhost:8888/notebooks/course-nlp/2-svd-nmf-topic-modeling.ipynb


https://shichaoji.com/tag/topic-modeling-python-lda-visualization-gensim-pyldavis-nltk/
https://github.com/bmabey/pyLDAvis/blob/master/notebooks/GraphLab.ipynb
https://github.com/bmabey/pyLDAvis/blob/master/notebooks/pyLDAvis_overview.ipynb

https://github.com/bmabey/pyLDAvis

"""

# topic modeling for humans
import gensim
from gensim import corpora

# visualize LDA
import pyLDAvis
import pyLDAvis.gensim

# viz
import matplotlib.pyplot as plt
import seaborn as sns

# import preprocessing pipeline
from data_pipeline.pre_processing_text.class_preprocessing import nlp_preprocessor

# tokenize a list
from data_pipeline.pre_processing_text.split_ngrams import tokenize_list


class topic_modeling_nlp:

    def __init__(self, model, preprocessing_pipeline=None):
        """
        Pipeline for topic modeling.
        Uses a default preprocessing class
        """

        self.model = model

        self._is_fit = False

        if not preprocessing_pipeline:
            self.preprocessor = nlp_preprocessor()
        else:
            self.preprocessor = preprocessing_pipeline


    def fit(self, X):
        """
        Train the vectorizer and model together using the 
        input training data.
        """
        self.preprocessor.fit(X)
        train_data = self.preprocessor.transform(X)
        self.model.fit(train_data)
        self._is_fit = True


    def transform(self, X):
        """
        Predicts on the data provided.
        """
        if not self._is_fit:
            raise ValueError("Must fit the model before transforming!")
        test_data = self.preprocessor.transform(X)
        preds = self.model.transform(test_data)
        return preds


    def print_topics(self, num_words=10):
        """
        Print out the top words for each topic
        """
        feat_names = self.preprocessor.vectorizer.get_feature_names()

        for topic_idx, topic in enumerate(self.model.components_):
            message = 'Topic #%d' % topic_idx
            message += " ".join([feat_names[i] for i in topic.argsort()[: -num_words - 1:-1]])
            
            print(message)

    
    def save_pipe(self, filename):
        """
        Save the pipeline.
        """
        if type(filename) != str:
            raise TypeError("Filename must be a string.")
        pickle.dump(self.__dict__, open(filename+".mdl", "wb"))

    def load_pipe(self, filename):
        """
        Load the pipeline.
        """
        if type(filename) != str:
            raise TypeError("Filke must be a string.")
        if filename[-4] != ".mdl":
            filename += ".mdl"
        self.__dict__ = pickle.load(open(filename, "rb"))





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