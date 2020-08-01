"""
Now that we have vectorized our corpus we can begin 
to transform it using models. 
We use model as an abstract term referring to a 
transformation from one document representation 
to another. In gensim documents are represented 
as vectors so a model can be thought of as a 
transformation between two vector spaces. 
The model learns the details of this transformation 
during training, when it reads the training Corpus.

One simple example of a model is tf-idf. 
The tf-idf model transforms vectors from the 
bag-of-words representation to a vector space 
where the frequency counts are weighted according 
to the relative rarity of each word in the corpus.

https://radimrehurek.com/gensim/auto_examples/core/run_core_concepts.html

"""

from gensim import models

def tfidf_model(list_of_strings):
    """
    Train a tfidf model
    Input:
        bow_corpus: term matrix
    Output:
        vector
    """

    dictionary, doc_term_matrix = doc2bow_vectorize(list_of_strings)

    # train the model
    tfidf = models.TfidfModel(doc_term_matrix)

    return tfidf[dictionary.boc2bow()]



from gensim import models

# train the model
tfidf = models.TfidfModel(doc_term_matrix)

# transform the "system minors" string
print(tfidf[dictionary.doc2bow(words)])