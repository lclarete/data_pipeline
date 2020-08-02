"""
Class to perform topic modeling.
"""

from data_pipeline.pre_processing_text.class_preprocessing import nlp_preprocessor


class topic_modeling_nlp:

    def __init__(self, moel, preprocessing_pipeline=None):
        """
        Pipeline for topic modeling.
        Uses a default preprocessing class
        """

        self.model = model

        self._is_fit = False

        if not preprocessing_pipeline:
            self.preprocessing = nlp_preprocessor()
        else:
            self.preprocessing = preprocessing_pipeline

    def fit(self, X):
        """
        Train the vectorizer and model together using the 
        input training data.
        """
        self.preprocessing.fit(X)
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
        feat_names = self.preprocessor.vectorizer.get_features_names()
        for topic_idx, topic in enumerate(self.model.componets_):
            message = 'Topic #%d' % topic_idx
            message += " ".join([feat_names[i] for i in topic.argsort()[: -num_words - 1: -1]])
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