"""
Stripping accents is still a method tha I have to explore more.

Not that useful for NLP in English, but for sure it is important
to normalize words in Portuguese and other languages that share 
the same accent feature.

Perhaps not so useful after normalizing words.


"""

import unicode

def strip_accent(text):
    '''
    Removes accents using unidecode
    '''
    return ''.join(i for i in unidecode.unidecode(text))

