import pandas as pd
import pytrends
from pytrends.request import TrendReq
import os
from datetime import date, datetime


######################### ----- Format Functions ----- ##################################

def group_keywords(keywords):
    """
    Create a list of lists containing one keywords in each one. 
    Used for more than 5 keywords.
    """
    groupkeywords = list(zip(*[iter(keywords)]))
    return [list(x) for x in groupkeywords]

def format_dict_query(dict_query, keywords, gprop='GoogleWeb'):
    """
    Format the query dictionary.
    """
    df = pd.DataFrame()

    for k in range(1, len(dict_query)):
        keyword = keywords[k]
        try:
            new_df = pd.concat(dict_query[k+1][keyword], sort=False).reset_index().drop('level_1', axis=1)
            new_df['keyword'] = keyword
            new_df['gprop'] = gprop
            df = pd.concat([new_df, df], sort=False)
        except:
            pass
    return df

def dict_to_dataframe(d, keywords, type_result='ts', gprop='GoogleWeb'):
    """
    Transform the dictionary into a formated dataframe.
    type_result could be equal to 'ts', 'query', or 'region'.
    """
    if type_result=='query':
        # apply function to format the 'query' dataframe
        return format_dict_query(d, keywords, gprop)
    
    # concat the dictionary
    result = pd.concat(d, axis=1)
    # flatten a hierarchical index in columns
    result.columns = result.columns.get_level_values(1)
    # rest the index
    result.reset_index(level=0, inplace=True)
    # new column describe the type of Google data
    result['gprop'] = gprop
    
    if type_result=='ts':
        # if it is a time series (ts) transform the columns into lines and drop 'isPartial columns' from the 'ts' dataframe
        result = result.drop('isPartial', axis=1)
        # return pd.melt(result, id_vars='date', value_vars=keywords, var_name=gprop)
        result = pd.melt(result, id_vars='date', value_vars=keywords)
        result['gprop'] = gprop
        return result

    if type_result=='region':
        # if it is equal to 'region', just return the results
        return result

def string_to_datetime(string_date, date_format="%Y-%m-%d %H:%M"):
    return datetime.strptime(string_date, date_format)


######################### ----- Request Functions ----- ##################################
def trends():
    """Instantiate TrendReq() class from pytrends.request"""
    return TrendReq()

def build_pytrend(keyword, timeframe, geo, gprop=''):
    """Call the ~build_payload~ method over the trends() function"""
    pytrend = trends()
    pytrend.build_payload(kw_list=keyword, timeframe=timeframe, geo=geo, gprop=gprop)
    return pytrend

def request_func(func, keywords, timeframe, geo, gprop, type_result='ts'):
    """Returns a dictionary with all the interested over time for each keyword"""
    
    labels = keywords
    
    # if the number of keywords exceeds 5
    # if len(keywords) >= 5:
    keywords = group_keywords(keywords)
    
    d = {}
    i = 1
    # call the TrendReq() function from the pytrends.request lib
    for keyword in keywords:
        d[i] = func(keyword, timeframe=timeframe, geo=geo, gprop=gprop)
        i+=1
        
    return dict_to_dataframe(d, labels, type_result, gprop)



######################### ----- Specific Functions ----- ##################################

def time_series(keyword, timeframe, geo, gprop=''):
    """Build the function to return the popularity over time"""
    return build_pytrend(keyword, timeframe, geo, gprop).interest_over_time()

def ts_web_youtube(keywords, timeframe, geo):
    """Returs the requests from Google Web and YouTube"""
    df_ts = request_func(time_series, keywords, timeframe, geo, '', type_result='ts')
    df_ts['gprop'] = 'GoogleWeb'
    df_ts_yt = request_func(time_series, keywords, timeframe, geo, 'YouTube', type_result='ts')
    return df_ts.append(df_ts_yt)


def region(keyword, timeframe, geo, gprop=''):
    """Build the function to return data by region"""
    return build_pytrend(keyword, timeframe, geo, gprop='').interest_by_region()

def related_query(keyword, timeframe, geo, gprop=''):
    """Build the function to return data by region"""
    return build_pytrend(keyword, timeframe, geo, gprop).related_queries()

def related_topics(keyword, timeframe, geo, gprop=''):
    """Build the function to return data by region"""
    return build_pytrend(keyword, timeframe, geo, gprop).related_topics()


######################### ----- Suggestion functions ----- ##################################

def suggestion(keyword):
    """Returns the suggestion keywords for a specific keyword"""
    suggest = trends().suggestions(keyword)
    df = pd.DataFrame(suggest)
    df['keyword'] = keyword
    return df

def suggest_keywords(keywords):
    """
    Interates over several keywords and 
    returns the related keywords
    """
    l = []
    for k in keywords:
        df_k = suggestion(k)
        l.append(df_k)
        
    df = pd.concat(l, sort=False)
    df.drop(columns='mid', inplace=True)
    
    return df


# Instable function, as only works with short periods of time. Work on the 'sleep' parameter
def hourly(keyword, start_date, end_date, geo, sleep, gprop='', cat=0):
    """
    Returns hourly popularity.
    start_time and end_time should follow this format: YYYYMMDD
    Choose short periods of time, such as a month.
    Otherwise you may receive a time out error
    'HTTPSConnectionPool(host='trends.google.com', port=443): Read timed out. (read timeout=5)'
    """
    start_date = string_to_datetime(start_date)
    end_date = string_to_datetime(end_date)
    
    return trends().get_historical_interest(
        keyword, 
        year_start=start_date.year, 
        month_start=start_date.month, 
        day_start=start_date.day, 
        hour_start=start_date.hour, 
        
        year_end=end_date.year, 
        month_end=end_date.month, 
        day_end=end_date.day, 
        hour_end=end_date.hour, 
        
        cat=cat, 
        geo=geo, 
        gprop=gprop, 
        sleep=sleep)
    


######################### ----- Call pytrends Function ----- ##################################

def call_pytrends(keywords, timeframe, geo, gprop='', type_result='ts'):
    df_ts = ts_web_youtube(keywords, timeframe, geo)
    df_r = request_func(region, keywords, timeframe, geo, gprop, type_result='region')
    df_rq = request_func(related_query, keywords, timeframe, geo, gprop, type_result='query')
    df_rt = request_func(related_topics, keywords, timeframe, geo, gprop, type_result='query')
    suggestions = suggest_keywords(keywords)
    return df_ts, df_r, df_rq, df_rt, suggestions


######################### ----- Format datasets ----- ##################################

cols = ['type', 'date', 'date_ts', 'keyword', 'value', 'gprop', 'top_rising_query', 'description', 'topic_title', 'topic_type']

def normalize_df(df, rename_cols, new_cols, cols=cols):
    """Returns a df with new columns, and reorder them"""
    
    # rename columns
    df.rename(columns=rename_cols, inplace=True)
    
    # add new columns based on a dictionary
    df = df.assign(**(new_cols))
    
    # reorder the columns
    return df.reindex(columns=cols)


######################### ----- Retrive and format datasets ----- ##################################



def main(rename_cols, new_cols, keywords, timeframe, geo, gprop):
    """Return a single sheet with all the values"""

    # call pytrends
    df_ts, df_r, df_rq, df_rt, sug_kw = call_pytrends(
        keywords=keywords, 
        timeframe=timeframe, 
        geo=geo, 
        gprop=gprop)

    # list with all dfs
    dfs_list = [df_ts, df_r, df_rq, df_rt, sug_kw]

    # format region dataset
    region_format = df_r.drop(columns='gprop').melt(id_vars='geoName')

    l = []
    for i in range(len(dfs_list)):
        # append the formated datasets
        l.append(
            normalize_df(
                df=dfs_list[i],
                rename_cols=rename_cols[i],
                new_cols=new_cols[i])
        )
    
    # return the concated datasets
    return pd.concat(l)

######################### ----- Trending Function ----- ##################################
# https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=all

def trending_search(pn='united_states'):
    """Returns real time search trends"""
    trending = trends().trending_searches(pn)
    trending.columns = ['trending topic']
    trending['date'] = today
    return trending

def today_search(pn='united_states'):
    """Returns the dayly search"""
    return trends().today_searches()

######################### ----- Top chart Function ----- ##################################
# https://trends.google.com/trends/yis/2019/GLOBAL/
# how to specify each category, such as cities, movies, scientists, etc.

def top_chart(year, hl, tz, geo):
    """Build the function to return data by region"""
    return trends().top_charts(year, hl=hl, tz=tz, geo=geo)

def yearly_top_charts(hl, tz, geo):
    """Call the top charts for each year and return a df"""
    df_top_charts = pd.DataFrame()

    for year in range(2011, 2020):
        a = top_chart(year, hl, tz, geo)
        a['year'] = year
        df_top_charts = pd.concat([df_top_charts, a], sort=False)
        
    return df_top_charts