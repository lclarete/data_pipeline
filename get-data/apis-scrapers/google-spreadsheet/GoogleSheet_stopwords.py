import pygsheets
from nltk.corpus import stopwords

def stop_words_gsheet():
    url = '/Users/liviaclarete/gdrive/code/functions/gdocs/googleKey_pesq7/client_secret.json'
    # reading stopwords from a google sheet
    gc = pygsheets.authorize(client_secret=url)
    # Open spreadsheet and then workseet
    sh = gc.open('stopwords_pt')
    wks = sh.sheet1
    # get the values
    stopwords_m = wks.get_all_values(returnas='matrix')
    # create a list with stopwords
    sheet_stopwords = [i[0] for i in stopwords_m]
    # loading nltk stopwords
    stop = stopwords.words('portuguese')
    stopwords_total = stop + sheet_stopwords
    return(stopwords_total)