from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from sys import path
path.append('/Users/liviaclarete/gdrive/code/functions')
from GoogleSheet_stopwords import stop_words_gsheet as pt_stopwords

class WordCloudPortuguese(col, stop_words=True, max_words=50):
    def __init__(sefl, data):
        self.data = data

    def load_data(self):
        string_text = str(col)
        self.string_test = string_text

    def word_cloud_figure(self, string_text, stop_words):
        pt_word_cloud = WordCloud(max_words=max_words,
                                stopwords=pt_stopwords,
                                )
        self.pt_word_cloud = pt.pt_word_cloud
    

