from pytrends_functions import main
from export_csv_files import export_one_csv, export_several_csv
from gsheets_functions import export_one_tab
from datetime import date, datetime

######################### ----- Parameters ----- ##################################

## keywords:
# https://support.google.com/trends/answer/4359582?hl=en

# specify a topic instead of a keyword: use the code 'topic_mid' instead of a keyword
# https://stackoverflow.com/questions/47389000/pytrends-how-to-specify-a-word-as-a-topic-instead-of-a-search-term

keywords = ['dermatite atopica', 'dermatite']

# geolocation
geo = 'BR'

# timeframe
timeframe = 'today 5-y'

# time zone
tz = 300

# Preferred language
# https://sites.google.com/site/tomihasa/google-language-codes
hl = 'pt-BR'

# used for trendings
pn = 'brazil'

# type of search
# 'images', 'news', 'youtube', 'froogle'
gprop = ''

# define the date
today = date.today()


# Gsheet parameters
new_sheet_name = 'dashboards_google_trends_test'
# new_tab_list = ['interest_over_time', 'interest_by_region', 'related_queries', 'related_topics', 'suggestions']
new_tab = 'pytrend_data'

######################### ----- Format parameters ----- ##################################

rename_cols_ts = {'variable': 'keyword', 'date':'date_ts'}

new_cols_ts = {
    'date': date.today(), 
    'level_0': '',
    'query': '',
    'type':'ts',
    'topic_title': '',
    'topic_type': ''
}

rename_col_query = {'level_0': 'top_rising_query', 'query': 'description'}

new_cols_query = {
    'date': date.today(), 
    'date_ts': '',
    'type':'query',
    'gprop': 'GoogleWeb',
    'topic_title': '',
    'topic_type': ''
}


rename_cols_reg = {'variable': 'keyword', 'geoName': 'description'}

new_cols_reg = {
    'date': date.today(), 
    'date_ts': '',
    'type':'region',
    'gprop': 'GoogleWeb',
    'topic_title': '',
    'topic_type': ''
}

rename_cols_top = {'level_0': 'top_rising_query'}

new_cols_top = {
    'date': date.today(), 
    'date_ts': '',
    'type':'topic',
    'gprop': 'GoogleWeb',
}

rename_cols_sug = {'title': 'topic_title', 'type': 'topic_type'}

new_cols_sug = {
    'date': date.today(), 
    'date_ts': '',
    'type':'suggestion',
    'gprop': 'GoogleWeb',
}

new_cols = [new_cols_ts, new_cols_reg, new_cols_query, new_cols_top, new_cols_sug]
rename_cols = [rename_cols_ts, rename_cols_reg, rename_col_query, rename_cols_top, rename_cols_sug]

######################### ----- Retrieve data ----- ##################################


# dictionary with the label and dataframe

df_ts, df_r, df_rq, df_rt, suggested_keywords = call_pytrends(keywords, timeframe, geo, gprop)

all_data = {
    'interest_over_time': df_ts,
    'interest_by_region': df_r,
    'related_queries': df_rq,
    'related_topics': df_rt,
    'suggestions': suggested_keywords,
}


df = main(rename_cols, new_cols, keywords, timeframe, geo, gprop)

######################### ----- Export data ----- ##################################

# export the dict with all the data to a csv's files
export_several_csv(all_data)

# export a single file
export_one_csv(df, 'one_single_spreadsheet')


# export to a Google Spreadsheet
# export_one_tab(new_sheet_name, new_tab, df)
export_one_tab(new_sheet_name, new_tab, df)
