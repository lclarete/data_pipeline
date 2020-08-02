"""
Create a class to implement data pipeline.

https://github.com/ZWMiller/nlp_pipe_manager/blob/master/nlp_pipeline_manager/nlp_preprocessor.py

# Example 1:

# import pipeline
from data_pipeline.pre_processing_text.preprocessing_class import nlp_preprocessor

# import lemmatizer
from data_pipeline.pre_processing_text.norm_lemmatize import lemmatize_list

nlp = nlp_preprocessor()

## Including new parts into the pipeline:

# tfidf vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# instantiate the class with the TfidfVectorizer as a new vectorizer parameter
nlp = nlp_preprocessor(vectorizer=TfidfVectorizer(lowercase=False))

# fit the model
nlp.fit(lemmatize_list, list_of_strings)

# return the feature names
nlp.vectorizer.get_feature_names()

# return a table counting the number of features per document
nlp.bow_table(lemmatize_list, list_of_strings)

"""

from sklearn.feature_extraction.text import CountVectorizer
import pickle
import pandas as pd

from data_pipeline.pre_processing_text.preprocess_string_list import preprocessing_list, preprocessing_string
from data_pipeline.pre_processing_text.norm_lemmatize import lemmatize_string, lemmatize_list
from data_pipeline.pre_processing_text.split_ngrams import tokenize, tokenize_list
from data_pipeline.pre_processing_text.clean_list_stopwords import remove_stopwords_list
from data_pipeline.pre_processing_text.clean_list_regex import sub_list_strings_list_regex


class nlp_preprocessor:
        
    def __init__(self, vectorizer=CountVectorizer(), 
                 tokenizer=None, 
                 cleaning_function=None, 
                 lemmatizer=None):
        
        """
        A class for pipelineing data in NLP problems. 
        User provides a series of tools (functions), and the
        class manages all the training, transforming and 
        modificaion of the text data.

        Inputs:
        vectorizer: model to use for text vectorization 
        tokenizer: tokenizer to use; default is split into spaces
        cleaning_functions: how to clean the data
        """
        
        # if tokenizer is not defined,
        if not tokenizer:
            # use splitter_strings as default
            tokenizer = self.splitter_string
            
        self.tokenizer = tokenizer

        # if cleaning_function is not defined,
        if not cleaning_function:
            # use the function clean_text as default
            # TO DO: drop regex dict and stopwords data out of the .py files
            # TO DO: structure the files in a way I can read the regex and 
            # stopwords as arguments inside the function
            cleaning_function = self.clean_text
            
            
        # TO DO: test new cleaning functions
        self.cleaning_function = cleaning_function
            
            
        self.lemmatizer = lemmatizer
        self.vectorizer = vectorizer
        self._is_fit = False
                
    
    def splitter_string(self, string):
        """
        Default tokenizer that splits a string on spaces naively
        """
        return string.split(' ')


    def clean_text(self, lemmatizer, list_of_strings):
        """
        Clean regex patterns, lemmatize words and remove stopwords
        Input:
            lemmatizer: function to lemmatize words
            list_of_strings: list of strings
        Output:
            list of cleaned strings
        """
        # clean regex patterns
        clean_text = sub_list_strings_list_regex(list_of_strings)
        # lemmatize words
        clean_text = lemmatizer(clean_text)
        # remove stopwords
        return remove_stopwords_list(clean_text)
    
    
    # for some reason, I can't use self.lemmatizer
    # TO DO: drop lemmatizer as the function argument
    def fit(self, lemmatizer, list_of_strings):
        """
        Cleans the data and then fits the vectorizer with
        the user provided text
        """

        # Why should I not use self.lemmatizer here?
#         clean_text = self.cleaning_function(list_of_strings, self.tokenizer, self.lemmatizer)
        preprocessed_text = self.cleaning_function(lemmatizer, list_of_strings)

        self.vectorizer.fit(preprocessed_text)
        self._is_fit = True
    

    def transform(self, lemmatizer, list_of_strings, return_clean_text=False):
        """
        Cleans any provided data and then transforms data
        into a vectorized format based on the fit function.
        Returns vectorized form of the data.
        """
        if not self._is_fit:
            raise ValueError("Must fit the models before transforming!")
#         clean_text = self.cleaning_function(list_of_strings, self.tokenizer, self.lemmatizer)
        clean_text = self.cleaning_function(lemmatizer, list_of_strings)

        if return_clean_text:
            return clean_text
        return self.vectorizer.transform(clean_text)

    
    def bow_table(self, lemmatizer, list_of_strings):
        """
        Apply the transformer to format a table counting the number of words per document
        Input:
            lemmatizer
            list_of_strings
        Output:
            table counting the number of words per document
        """
        data = self.transform(lemmatizer, list_of_strings).toarray()
        columns = self.vectorizer.get_feature_names()
        return pd.DataFrame(data, columns=columns)
    
    
    def save_pipe(self, filename):
        """
        Writes the attributes of the pipeline to a file
        allowing a pipeline to be loaded later with the
        pre-trained pieces in place.
        """
        if type(filename) != str:
                raise TypeError("filename must be a string")
        pickle.dump(self.__dict__, open(filename+'.mdl', 'wb'))

        
    def load_pipe(self, filename):
        """
        Writes the attributes of the pipeline to a file
        allowing a pipeline to be loaded later with the
        pre-trained pieces in place.
        """
        if type(filename) != str:
            raise TypeError("filename must be a string")
        if filename[-4:] != '.mdl':
            filename += '.mdl'
        self.__dict__ = pickle.load(open(filename,'rb'))


