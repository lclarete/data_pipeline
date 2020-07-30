# reads data from google sheet and returns a dataframe
import pygsheets
import pandas as pd
'''
Reads a google sheet and returs a dataframe
'''

def gsheet_returns_df(sheet_name, tab_name):
    # point the client_secret.json
    url = '/Users/liviaclarete/gdrive/code/functions/gdocs/googleKey_pesq7/client_secret.json'
    # reading stopwords from a google sheet
    gc = pygsheets.authorize(client_secret=url)
    # Open spreadsheet and then workseet
    sh = gc.open(sheet_name)
    wks = sh.worksheet('title', tab_name)
    # get the values as a df
    gsheet_matrix = wks.get_as_df()
    return(gsheet_matrix)