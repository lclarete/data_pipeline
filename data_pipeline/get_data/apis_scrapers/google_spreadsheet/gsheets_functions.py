import pygsheets
import numpy as np
import pandas as pd

url = '/Users/liviaclarete/coding/functions/gdocs/googleKey_pesq7/client_secret.json'

##################### ----- Authorize and open functions ----- #####################

def authorize_client(url=url):
    """Authorize the client secret"""
    return pygsheets.authorize(client_secret=url)

def open_gsheet(sheet_name, url=url):
    """Open a spreadsheet"""
    return authorize_client(url).open(sheet_name)

def open_tab(sheet_name, tab_name, url=url):
    """Open a tab"""
    return open_gsheet(sheet_name, url).worksheet('title', tab_name)


##################### ----- Create and delete sheets and tabs ----- #####################

def create_new_sheet(new_sheet_name_list, folder=None, url=url):
    """Create new spreadsheet"""
    if type(new_sheet_name_list) == list:
        for sheet in new_sheet_name_list:
            authorize_client(url=url).create(sheet, folder=folder)
    if type(new_sheet_name_list) == str:
        authorize_client(url=url).create(new_sheet_name_list, folder=folder)
    pass
        
def create_new_tabs(sheet_name, new_tab_list):
    """Create new tabs"""
    for tab in new_tab_list:
        open_gsheet(sheet_name).add_worksheet(tab)
    pass

def delete_tabs(sheet_name,  url=url):
    return open_gsheet(sheet_name, url).del_worksheet(new_tab_list)
    
    
##################### ----- Permission function ----- #####################

def share_spreadsheet(list_of_emails, sheet_name, url=url):
    """Share the spreadsheet with a list of emails"""
    for email in list_of_emails:
        open_gsheet(sheet_name, url).share(email)
        

def remove_permission(list_of_emails, sheet_name, url=url):
    """Remove permission based on a list of emails"""
    for email in list_of_emails:
        open_gsheet(sheet_name, url).remove_permission(email)
    pass

##################### ----- Read and write data function ----- #####################

def get_df_gsheets(sheet_name, tab_name, url=url):
    """Download data in format of a data frame"""
    return open_tab(sheet_name, tab_name, url).get_as_df()

def write_gsheet(sheet_name, tab_name, df, url=url):
    """Write a df into a spreadsheet"""
    return open_tab(sheet_name, tab_name, url).set_dataframe(df, (1,1))

def clear_gsheets(sheet_name, tab_name, url=url):
    """Clean the values from a spreadsheet"""
    return open_tab(sheet_name, tab_name, url).clear()

def export_several_gsheets(sheet_name, dict_data):
    """
    Loop over a dictionary composed of tab_names and dfs
    export the dataframes to a spreadsheet tab
    """
    for tab_name, df in dict_data.items():
        # clean the sheets
        clear_gsheets(sheet_name, tab_name)
        # write the new content
        write_gsheet(sheet_name, tab_name, df)
    pass

def export_several_tabs(new_sheet_name, new_tab_list, dict_data):
    """Export a file with multiple tabs"""
    # create a new spreadsheet
    create_new_sheet(new_sheet_name)
    # create new list of tabs
    create_new_tabs(new_sheet_name, new_tab_list)
    # write the files into each tab
    export_several_gsheets(new_sheet_name, dict_data)



def export_one_tab(sheet_name, tab_name, df, exist_sheet=False, url=url):
    """Export a file with only one tab"""
    
    if exist_sheet==True:
        # clean the existing data
        clear_gsheets(sheet_name, tab_name)
        
        # write the new one
        write_gsheet(sheet_name, tab_name, df)
    
    else:
        # create a new spreadsheet
        authorize_client(url=url).create(sheet_name, folder=None)

        # create one tab
        open_gsheet(sheet_name).add_worksheet(tab_name)

        # write the file into a new tab
        write_gsheet(sheet_name=sheet_name, tab_name=tab_name, df=df, url=url)

    pass