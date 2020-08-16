"""
Load GloVe models

embedding_dictionary['king']

array([-0.32307 , -0.87616 ,  0.21977 ,  0.25268 ,  0.22976 ,  0.7388  ,
       -0.37954 , -0.35307 , -0.84369 , -1.1113  , -0.30266 ,  0.33178 ,
       -0.25113 ,  0.30448 , -0.077491, -0.89815 ,  0.092496, -1.1407  ,
       -0.58324 ,  0.66869 , -0.23122 , -0.95855 ,  0.28262 , -0.078848,
        0.75315 ,  0.26584 ,  0.3422  , -0.33949 ,  0.95608 ,  0.065641,
        0.45747 ,  0.39835 ,  0.57965 ,  0.39267 , -0.21851 ,  0.58795 ,
       -0.55999 ,  0.63368 , -0.043983, -0.68731 , -0.37841 ,  0.38026 ,
        0.61641 , -0.88269 , -0.12346 , -0.37928 , -0.38318 ,  0.23868 ,
        0.6685  , -0.43321 , -0.11065 ,  0.081723,  1.1569  ,  0.78958 ,
       -0.21223 , -2.3211  , -0.67806 ,  0.44561 ,  0.65707 ,  0.1045  ,
        0.46217 ,  0.19912 ,  0.25802 ,  0.057194,  0.53443 , -0.43133 ,
       -0.34311 ,  0.59789 , -0.58417 ,  0.068995,  0.23944 , -0.85181 ,
        0.30379 , -0.34177 , -0.25746 , -0.031101, -0.16285 ,  0.45169 ,
       -0.91627 ,  0.64521 ,  0.73281 , -0.22752 ,  0.30226 ,  0.044801,
       -0.83741 ,  0.55006 , -0.52506 , -1.7357  ,  0.4751  , -0.70487 ,
        0.056939, -0.7132  ,  0.089623,  0.41394 , -1.3363  , -0.61915 ,
       -0.33089 , -0.52881 ,  0.16483 , -0.98878 ], dtype=float32)

"""

from keras.preprocessing.text import Tokenizer
import numpy as np

def load_glove_file(url):
    """
    Load GloVe file.
    Input:
        url: place where the GloVe file is located
    Output:
        dictionary: words as keys, and vectors as values
    """
    embedding_dictionary = dict()
    glove_file = open(url, encoding='utf8')

    for line in glove_file:
        records = line.split()
        word = records[0]
        vector_dimentions = np.asarray(records[1:], dtype='float32')
        embedding_dictionary[word] = vector_dimentions
    
    glove_file.close()
    
    return embedding_dictionary


def load_embedding_matrix(list_of_strings, vocab_size, url):
    """
    Look for the words within the corpus and returns 
    the respective arrays from the loaded model
    
    Inputs:
        list_of_strings: corpus
        vocab_size: number of unique words
        url: word embedding url
    
    Output:
        matrix with imported words
    """

    # preprocess class
    word_token = Tokenizer()
    word_token.fit_on_texts(list_of_strings)

    embedding_dictionary = load_glove_file(url)

    embedding_matrix = np.zeros((vocab_size, 100))
    for word, index in word_token.word_index.items():
        embedding_vector = embedding_dictionary.get(word)
        if embedding_vector is not None:
            embedding_matrix[index] = embedding_vector
    
    return embedding_matrix