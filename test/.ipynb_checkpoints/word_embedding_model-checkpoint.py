"""
### Creating a Sequential model
* Add Embedding layer
* Flatten the Embedding layer
* Add a Dense layer


## Word Embedding with Keras Functional API
According to this author over there, Sequential API 
is mostly used for beginners. 
The advanced models usually use Functional APIs. 
So, here we go to create a second model :)

https://stackabuse.com/python-for-nlp-word-embeddings-for-deep-learning-in-keras/

"""

# Neural Network model

# preprocessing
from nltk.tokenize import word_tokenize
from word_embedding_preprocessing import vocab_size_func, longest_sentence_func


# model libs
from keras.models import Sequential, Model, Input
from keras.layers import Dense, Dropout, Flatten
from keras.layers.embeddings import Embedding
from keras.optimizers import Adam


def create_sequencial_model(list_of_strings, vocab_size, learn_rate, embedding_matrix):

    # create a model
    model = Sequential()

    # ADD LAYERS TO THE MODEL
    
    # word embeddings inputs
    # vocab_size = vocab_size_func(list_of_strings)
    _, len_long_sentence =  longest_sentence_func(list_of_strings)
    
    # add the Embedding layer
    model.add(Embedding(
        # size of the vocabulary
        ## or the total number of unique words in a corpus
        vocab_size, 
        # number of dimensions for each word vector to be created
        20, 
        # len of the longest sentence
        input_length=len_long_sentence,
        weights=[embedding_matrix]
        ))

    # flatten the layer so it can be used directly with 
    # the densely connected layer
    # as we can see in the summary, the flatten array has a shape of 140
    # instead of (7, 20)
    # the flatten array is directly connected to the Dense layer
    model.add(Flatten())

    # add a Dense layer
    model.add(Dense(
        # https://keras.io/guides/sequential_model/
        # Not sure aht this 1 is. The author call it 'neuran'
        # maybe it is a 'neuron' as 'neuran' looks like a typo
        # but it impacts on the number of trainable parameters
        1,
        # as it is a binary classification, 
        # we use sigmoid as the loss fucntion
        activation='sigmoid'))
    

    # COMPILE THE MODEL
    adam = Adam(lr=learn_rate)
    
    model.compile(
        optimizer=adam,
        # loss function for binary classification
        loss='categorical_crossentropy',
        metrics=['acc']
    )
    
    return model


# functional API
def create_functional_model(list_of_strings, vocab_size, embedding_matrix):
    """
    Create a functional model
    
    Inputs:
        list_of_strings: list of texts
        vocab_size: number of vocab unique words
        embedding_matrix: loaded vectors from GloVe
        
    Outputs:
        
        
    """
    # set the input
    # not sure what does that mean
    
    _, len_long_sentence =  longest_sentence_func(list_of_strings)

    # In Function API, we have to define the input layer separately
    # before the embedding layer
    # simply pass the length of the input vector
    deep_inputs = Input(shape=(len_long_sentence,))

    # set the Embedding layer
    embedding = Embedding(vocab_size, 100, 
                          # this is the glove loaded vectors
                          weights=[embedding_matrix], 
                          input_length=len_long_sentence, 
                          trainable=False)(deep_inputs) # line A

    flatten = Flatten()(embedding)


    hidden = Dense(1, activation='sigmoid')(flatten)
    model = Model(inputs=deep_inputs, outputs=hidden)

    # Compile data
    model.compile(
        optimizer='adam', 
        loss='crossentropy',
        metrics=['acc'])
    
    return model