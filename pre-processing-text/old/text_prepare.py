import nltk
import pickle
import re
import numpy as np
import string

nltk.download('stopwords')
from nltk.corpus import stopwords


def text_prepare(text):
    """Perform tokenizatio and simple preprocessing"""
    
    # set the regular expressions
    remove_hyperlinks_re = re.compile(r'https?:\/\/.*[\r\n]*')
    replace_by_space_re = re.compile('[/(){}\[\]\|@,;]')
    bad_symbols_re = re.compile('[^0-9a-z #+_a]')
    stopwords_set = set(stopwords.words('english'))
    
    
    # lower the string
    text = text.lower()

    # remove hyperlinks
    text = remove_hyperlinks_re.sub('', text)

    # replace space
    text = replace_by_space_re.sub(' ', text)
    
    # replace numbers and symbels
    text = bad_symbols_re.sub('', text)
    
    # remove stopwords
    text = ' '.join([t for t in text.split() if t not in stopwords_set])
    
    # remove old style retweet text "RT"
    text = re.sub(r'^RT[\s]+', '', text)

    # remove only the hash # sign from the hashtag
    text = re.sub(r'#', '', text)

    
    return text.strip()

stopwords_english = set(stopwords.words('english'))

def text_prepare_v2(text, stopwords=stopwords_english):
    """ 
    Clean text from a Pandas dataframe.
    Remove @ followed by the profil's name
    """

#     text = df[text_col]

    # lower text
    text = text.lower()
    
    # remove hiperlinks
    text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)

    # remove punctuation
    text = text.replace('[^\w\s]', '')

    # remove square brackets, punctuation and quotes
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)

    # remove stopwords
    text = ' '.join([w for w in text.split() if w not in stopwords])

    # remove symbols
    text = re.sub('[^0-9a-z #+_a]', '', text)
#     df['text'] = text
    
#     return df
    return text



######################### --- Old cleaning function --- #########################

import re
import string
import unidecode
import spacy
from nltk.corpus import stopwords

# strip links and mentions from text
def strip_link_mentions(text):
    mention_pattern = r'@(\w+)'
    url_pattern = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:\'\".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"""
    return re.sub(mention_pattern, '', text)

def strip_punct(text):
    text_clean = []
    for p in string.punctuation:
        text = text.replace(p, '').lower()
    return text

# strip symbols
def strip_symbols(text):
    return text.replace('“','').replace('#', '').replace('\n', '')

# strip digits
def strip_digits(text):
    return ''.join(re.sub(r'\d+', '', text))

def lemmatization(col):
    nlp = spacy.load('pt_core_news_sm')
    lemma = ''
    for token in nlp(col):
        lemma += token.lemma_ + ' '
    return lemma

def correct_lemma(text):
    w_wrong = ['pintar']
    w_right = ['pinto']
    for i in range(0, len(w_wrong)):
        text = re.sub(w_wrong[i], w_right[i], text)
    return text

def strip_sw(text):
    sw_pt = stopwords.words('portuguese') 
    sw = sw_pt + ['pra', 'portanto', 'rt', 'ah', 'poder', 'ser', 'ter', 'ir']
    return ' '.join(w for w in text.split() if w not in sw)


def strip_accent(text):
    '''a function that removes accents using unidecode'''
    return ''.join(i for i in unidecode.unidecode(text))

# gether the results from the remove links, sw, strip accent and punctuation
def cleaning_tweets(col):
    col_clean = strip_link_mentions(col)
    col_clean = strip_punct(col_clean)
    col_clean = strip_symbols(col_clean)
    col_clean = strip_digits(col_clean)
    col_clean = lemmatization(col_clean)
    col_clean = correct_lemma(col_clean)
    col_clean = strip_sw(col_clean)
    col_clean = strip_accent(col_clean)
    return(col_clean)



######################### --- Text Scipy cleaning functions --- #########################

