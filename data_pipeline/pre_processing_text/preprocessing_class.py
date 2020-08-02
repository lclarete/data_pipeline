"""
Create a class to implement data pipeline.

https://github.com/ZWMiller/nlp_pipe_manager/blob/master/nlp_pipeline_manager/nlp_preprocessor.py

"""

from sklearn.feature_extraction.text import CountVectorizer
import pickle

class nlp_preprocessor_CountVectorizer:
        
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
            cleaning_function = self.clean_text
        self.cleaning_function = cleaning_function
            
        self.lemmatizer = lemmatizer
        self.vectorizer = vectorizer
        self._is_fit = False
        
    
    def splitter_string(self, string):
        """
        Default tokenizer that splits a string on spaces naively
        """
        return string.split(' ')


    def clean_text(self, list_of_strings, tokenizer, lemmatizer):
        """
        A naive function to lowercase all works can clean them quickly.
        This is the default behavior if no other cleaning function is specified
        """
        cleaned_text = []
        for string in list_of_strings:
            cleaned_words = []
            for word in tokenizer(string):
                low_word = word.lower()
                if lemmatizer:
                    low_word = lemmatizer(low_word)
                cleaned_words.append(low_word)
            cleaned_text.append(' '.join(cleaned_words))
        return cleaned_text


    def fit(self, list_of_strings):
        """
        Cleans the data and then fits the vectorizer with
        the user provided text
        """
        clean_text = self.cleaning_function(list_of_strings, self.tokenizer, self.lemmatizer)
        self.vectorizer.fit(clean_text)
        self._is_fit = True
    

    def transform(self, list_of_strings, return_clean_text=False):
        """
        Cleans any provided data and then transforms data
        into a vectorized format based on the fit function.
        Returns vectorized form of the data.
        """
        if not self._is_fit:
            raise ValueError("Must fit the models before transforming!")
        clean_text = self.cleaning_function(list_of_strings, self.tokenizer, self.lemmatizer)
        
        if return_clean_text:
            return clean_text
        return self.vectorizer.transform(clean_text)

    
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




################# ORIGINAL FUNCTION ###################

# from sklearn.feature_extraction.text import CountVectorizer
# import pickle

# class nlp_preprocessor:
   
#     def __init__(self, vectorizer=CountVectorizer(), tokenizer=None, cleaning_function=None, 
#                  stemmer=None, model=None):
#         """
#         A class for pipelining our data in NLP problems. The user provides a series of 
#         tools, and this class manages all of the training, transforming, and modification
#         of the text data.
#         ---
#         Inputs:
#         vectorizer: the model to use for vectorization of text data
#         tokenizer: The tokenizer to use, if none defaults to split on spaces
#         cleaning_function: how to clean the data, if None, defaults to the in built class
#         """
#         if not tokenizer:
#             tokenizer = self.splitter
#         if not cleaning_function:
#             cleaning_function = self.clean_text
#         self.stemmer = stemmer
#         self.tokenizer = tokenizer
#         self.model = model
#         self.cleaning_function = cleaning_function
#         self.vectorizer = vectorizer
#         self._is_fit = False
        
#     def splitter(self, text):
#         """
#         Default tokenizer that splits on spaces naively
#         """
#         return text.split(' ')
        
#     def clean_text(self, text, tokenizer, stemmer):
#         """
#         A naive function to lowercase all works can clean them quickly.
#         This is the default behavior if no other cleaning function is specified
#         """
#         cleaned_text = []
#         for post in text:
#             cleaned_words = []
#             for word in tokenizer(post):
#                 low_word = word.lower()
#                 if stemmer:
#                     low_word = stemmer(low_word)
#                 cleaned_words.append(low_word)
#             cleaned_text.append(' '.join(cleaned_words))
#         return cleaned_text
    
#     def fit(self, text):
#         """
#         Cleans the data and then fits the vectorizer with
#         the user provided text
#         """
#         clean_text = self.cleaning_function(text, self.tokenizer, self.stemmer)
#         self.vectorizer.fit(clean_text)
#         self._is_fit = True
        
#     def transform(self, text):
#         """
#         Cleans any provided data and then transforms the data into
#         a vectorized format based on the fit function. Returns the
#         vectorized form of the data.
#         """
#         if not self._is_fit:
#             raise ValueError("Must fit the models before transforming!")
#         clean_text = self.cleaning_function(text, self.tokenizer, self.stemmer)
#         return self.vectorizer.transform(clean_text)
    
#     def save_pipe(self, filename):
#         """
#         Writes the attributes of the pipeline to a file
#         allowing a pipeline to be loaded later with the
#         pre-trained pieces in place.
#         """
#         if type(filename) != str:
#             raise TypeError("filename must be a string")
#         pickle.dump(self.__dict__, open(filename+".mdl",'wb'))
        
#     def load_pipe(self, filename):
#         """
#         Writes the attributes of the pipeline to a file
#         allowing a pipeline to be loaded later with the
#         pre-trained pieces in place.
#         """
#         if type(filename) != str:
#             raise TypeError("filename must be a string")
#         if filename[-4:] != '.mdl':
#             filename += '.mdl'
#         self.__dict__ = pickle.load(open(filename,'rb'))