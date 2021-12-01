"""
Create a class to implement data pipeline.

from the class' author
This allows us to sweep all of the preprocessing into a class where we can control the pieces and parts that go in, and can see what comes out. If we wanted to, we could even add a model into the class as well and put the whole pipe into a single class that manages all of our challenges. In this case, we've left it outside for demo purposes. This also saves all of the pieces together, so we can just pickle a class object and that will keep the whole structure of our models together - such as the vectorizer and the stemmer we used, as well as the cleaning routine, so we don't lose any of the pieces if we want to run it on new data later.

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

import pickle
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer

from data_pipeline.pre_processing_text.preprocess_string_list import preprocessing_list, preprocessing_string
from data_pipeline.pre_processing_text.norm_lemmatize import lemmatize_string, lemmatize_list
from data_pipeline.pre_processing_text.split_ngrams import tokenize, tokenize_list
from data_pipeline.pre_processing_text.clean_list_stopwords import remove_stopwords_list
from data_pipeline.pre_processing_text.clean_list_regex import sub_list_strings_list_regex


class nlp_preprocessor:
        
    def __init__(self, 
                vectorizer=CountVectorizer(), 
                tokenizer=None, 
                cleaning_function=None, 
                lemmatizer=None):
        
        """
        A class for preprocessing data in NLP problems. 
        User provides a serie of tools (functions), and the
        class manages all the training, transforming and 
        modificaion of the text data.

        Inputs:
        vectorizer: model to use for text vectorization 
        tokenizer: tokenizer to use; default is split into spaces
        cleaning_functions: how to clean the data
        """

        # DATA
        
        # if tokenizer is not defined,
        if not tokenizer:
            # use splitter_strings as default
            tokenizer = self.splitter_string
            
        self.tokenizer = tokenizer

        # if cleaning_function is not defined,
        if not cleaning_function:
            # use the function clean_text as default
            # TO DO: drop regex dict and stopwords data out of the 
            # sub_list_strings_list_regex.py files
            # TO DO: structure the files in a way I can read the regex and 
            # stopwords as arguments inside the function
            cleaning_function = self.clean_text
            
            
        # TO DO: test new cleaning functions
        self.cleaning_function = cleaning_function
            
            
        self.lemmatizer = lemmatizer
        self.vectorizer = vectorizer
        self._is_fit = False
                
    # METHODS
    # TO DO: split words and punctuation
    def splitter_string(self, string):
        """
        Default tokenizer that splits a string on spaces naively
        """
        return string.split(' ')


    def clean_text(self, list_of_strings, lemmatizer=None):
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
        if lemmatizer:
            clean_text = lemmatizer(clean_text)
        # remove stopwords
        return remove_stopwords_list(clean_text)
    
    
    def fit(self, list_of_strings):
        """
        Cleans the data and then fits the vectorizer with
        the user provided text
        """

        # pay attention to the next function to be written
        # the lemmatizer is the first argument
        preprocessed_text = self.cleaning_function(list_of_strings, self.lemmatizer)

        self.vectorizer.fit(preprocessed_text)
        self._is_fit = True
    

    def transform(self, list_of_strings, return_preprocessed_text=False):
        """
        Cleans any provided data and then transforms data
        into a vectorized format based on the fit function.
        Returns vectorized form of the data.
        """
        if not self._is_fit:
            raise ValueError("Must fit the models before transforming!")
            
        preprocessed_text = self.cleaning_function(list_of_strings, self.lemmatizer)

        if return_preprocessed_text:
            return preprocessed_text
        
        return self.vectorizer.transform(preprocessed_text)

    
    def bow_table(self, list_of_strings):
        """
        Apply the transformer to format a table counting the number of words per document
        Input:
            lemmatizer
            list_of_strings
        Output:
            table counting the number of words per document
        """
        data = self.transform(list_of_strings).toarray()
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

