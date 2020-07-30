import pygsheets
import pandas as pd

def write_df_gsheet(sheet_name, tab_name, write_google_sheet):
    # point the client_secret.json
    url = '/Users/liviaclarete/gdrive/code/functions/gdocs/googleKey_pesq7/client_secret.json'
    # reading stopwords from a google sheet
    gc = pygsheets.authorize(client_secret=url)
    # Open spreadsheet and then workseet
    sh = gc.open(sheet_name)
    wks = sh.worksheet('title', tab_name)
    # get the values as a df
    upload_data = wks.update_values('A2', write_google_sheet)
    return(upload_data)