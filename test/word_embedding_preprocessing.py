"""
* Functions:
- vocab_size_func: return the size of the vocab
- one_hot_encode_vector_func: encode arrays
- padding_encoded_vector_func: return encoded and 
padded vocab

WORD EMBEDDING PARAMETERES

* 1st: vocabulary size
* 2nd: encoded vector

> a) Encoding word vector
> b) Standardize the size of each encoded array:

The embedding layer are expected to have equal size. 
However, it is not guaranteed to happen in the 
real world text analysis. 
In this case, we should standardize the length of all 
the sentences in the corpus.
Find the largest sentences and the increase 
the number lenght of all the sentences to the length 
of the largest one. 
"""

##### ---------- #####
from nltk.tokenize import word_tokenize
from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences


# FIRST PARAMETER OF THE EMBEDDING LAYER
def vocab_size_func(list_of_strings):
    """
    Count the number of unique words within a list of strings.
    The number of unique words is called 'vocabulary size'
    Input:
        list_of_strings: vocabulary
    Output:
        vocabulary size
    """
    # tokenize the list of words and append it in a list
    all_words = []
    for string in list_of_strings:
        # tokenize using the nltk function
        tokenized_string = word_tokenize(string)
        for word in tokenized_string:
            all_words.append(word)
    # create a list of unique words
    unique_words = set(all_words)
    # count the count words
    len_unique_words = len(unique_words)
    
    # return the number of unique words
    # known as the vocab size
    return len_unique_words


##### ---------- #####
# SECOND PARAMETER OF THE EMBEDDING LAYER

def one_hot_encode_vector_func(list_of_strings, vocab_size=True, extra_size=1):
    """
    Encode the list of strings. Basically, it replaces words per numbers.
    Each word will be encoded with the same number.
    Input:
        list_of_string: vocab
    Output:
        list arrays containing numbers
    """
    # get the vocab size
    if vocab_size==True:
        vocab_size = vocab_size_func(list_of_strings)
        vocab_size = vocab_size + extra_size
        
    # it is also possible to replace the one_hot per
    # Tokenizer -- from keras.preprocessing.text
    # word_token = Tokenizer()
    # word_token.fit_on_texts(corpus)
    # embedded_sentences = word_token.texts_to_sequences(corpus)


    # use the keras class 'one_hot' to process the text
    embedded_sentences = [one_hot(sent, vocab_size) for sent in list_of_strings]
    return embedded_sentences


def longest_sentence_func(list_of_strings):
    """
    Returns the longuest sentence and the size of it.
    """
    # 1. find the size of the longest sentence
    
    # define a lambda function to count the size of it
    word_count = lambda sentence: len(word_tokenize(sentence))
    # return the longest sentence
    longest_sentence = max(list_of_strings, key=word_count)
    # count the size of the longest sentence
    len_long_sentence = len(word_tokenize(longest_sentence))

    return longest_sentence, len_long_sentence


##### ---------- #####
def padding_encoded_vector_func(list_of_strings, extra_size=1):
    """
    Standardize the size of each vector by 
    padding the vectors with zeros in the end.
    
    In order to make the sentences of equal size, 
    the function pad_sequences can add zeros 
    to empty indexes that will be created as 
    a result of increasing the sentence length.
    
    Input:
        list_of_strings
    Output:
        list of vectors with zeros in the end
    """
    _, len_long_sentence =  longest_sentence_func(list_of_strings)
    # 2. padding the sentences with zeros based on the 
    # size of the longest sentence
    
    # embed the list_of_strings
    embedded_sentences = one_hot_encode_vector_func(list_of_strings, extra_size=extra_size)
    
    padded_sentences = pad_sequences(
        # list of encoded sentences with unequal size
        embedded_sentences,
        # include the size of the longest sentence
        len_long_sentence,
        # specify where to place the pad:
        # in the beginning or at the end of the array
        padding='post')
    
    # return the padded sentence
    return padded_sentences