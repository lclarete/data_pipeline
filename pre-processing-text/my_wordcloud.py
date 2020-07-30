"""
Wordcloud is the first attempt in visualizing a vocab.
"""

from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def wordcloud_figure(string_text,
            max_words=None,
            background_color='white',
            stopwords=None,
            save_file=False,
            ):

    """
    Create a wordcloud based on a string of text

    Input:
        string_text: string of text
        optionals:
            max_words: maximum of words to build a wordcloud
            background_color: color of the background - white as default
            stopwords: possibility to include a list of stopwords
    
    Output:
        plot a wordcloud image and/or save it as an image
    """
    # call the WordCloud function
    wordCloud = WordCloud(max_words=max_words,
                        repeat=False,
                        stopwords=stopwords,
                        background_color=background_color
                        ).generate(string_text)
    
    # define the viz parameters
    plt.figure(figsize=(10,7))
    plt.imshow(wordCloud, interpolation='bilinear')
    plt.axis('off')

    if save_file==True:
        plt.savefig('word_cloud')
        return plt.show()
    
    else:
        return plt.show()
    


