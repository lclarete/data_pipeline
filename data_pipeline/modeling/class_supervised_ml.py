"""
Class to perform supervised nlp.

"""

from data_pipeline.pre_processing_text.class_preprocessing import nlp_preprocessor

class supervised_nlp:
    def __init__(self, model, preprocessing_pipeline=None):
        """
        Pipeline to perform supervised nlp.
        Expects a model and create a preprocessing pipeline if one isn't provided
        """

        self.model = model
        self._is_fit = False

        if not preprocessing_pipeline:
            self.preprocessor = nlp_preprocessor()
        else:
            self.preprocessor = preprocessing_pipeline
        
    
    def fit(self, X, y):
        """
        Trains the vectorizer and model together using
        the users input training data.
        """

        self.preprocessor.fit(X)
        train_data = self.preprocessor.transform(X)
        self.model.fit(train_data, y)
        self._is_fit = True
    

    def predict(self, X):
        """
        Predicts based on the data provided using
        the preprocessing pipeline and model 
        passed as parameters.
        """

        if not self.is_fit:
            raise ValueError("Must fit the models before transforming!")
        test_data = self.preprocessor.transform(X)
        preds = self.model.predict(test_data)
        return preds


    def score(self, X, y):
        """
        Returns accuracy for the model after using the
        trained preprocessing pipeline to prepare the data
        """

        test_data = self.preprocessor.transform(X)
        return self.model.score(test_data, y)

    def save_pipe(self, filename):
        """
        Writes the attributes of the pipeline to a file
        allowing a pipeline to be loaded later with the
        pre-trained pieces in place.
        """

        if type(filename) !=str:
            raise TypeError("Filename must be a string.")
        pickle.dump(self.__dict__, open(filename+'.mdl', 'wb'))
    
    def load_pipe(self, filename):
        """
        Loads the pipeline into the model.
        """

        if type(filename) != str:
            raise TypeError("Filename must be a strign.")
        if filename[-4] != '.mdl':
            filename += '.mdl'
        self.__dict__ = pickle.load(open(filename, 'rb'))