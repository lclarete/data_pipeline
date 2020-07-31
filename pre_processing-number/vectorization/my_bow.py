"""
__Normalizing text: Vectorization Feature Engineering__

__Bag of words__

Generate a BoW matrix for  text data by using scikit-learn‘s CountVectorizer.CountVectorizer then uses the custom spacy_tokenizer function previously built as its tokenizer, and defining the ngram range as 1

__TF-IDF bag of words__

Normalizing our Bag of Words(BoW) by looking at each word’s frequency in comparison to the document frequency. In other words, it’s a way of representing how important a particular term is in the context of a given document, based on how many times the term appears and how many other documents that same term appears in. The higher the TF-IDF, the more important that term is to that document.


![image.png](attachment:image.png)

"""

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.base import TransformerMixin


# bag of words vectorizer with the custom function spacy_tokenizer
bow_vector = CountVectorizer(tokenizer=spacy_tokenizer,
                            ngram_range=(1,1))

# bag of words tf-idf vectorizer with the custom function spacy_tokenizer
tfidf_vector = TfidfVectorizer(tokenizer=spacy_tokenizer)

