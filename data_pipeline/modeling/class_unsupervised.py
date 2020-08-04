"""
Build a unsupervised class
"""

from data_pipeline.pre_processing_text.class_preprocessing import nlp_preprocessor
class unsupervised_ml:

    def __init__(
        self,
        model,
        preprocessing_pipeline=None,"
    )
        """
        Pipeline for unsupervised machine learning
        """

        self.model = model
        self._is_fit = False

        if not processing_pipeline:
            self.preprocessor = nlp_preprocessor()
        else:
            self.preprocessor = preprocessing_pipeline

    def fit(self, X):
        """
        Train the model
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