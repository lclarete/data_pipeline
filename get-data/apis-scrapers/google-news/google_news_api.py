def set_google_news(language, period, start_time, end_time):
    """
    Set the parameters for the GoogleNews() class.
    language: 'pt' or 'en'.
    start_time and end_time define the range of date that should be collected.
    search_term: term to retrive the news
    n_times: number of pages to be retrieved
    """
    
    # instantiate the GoogleNews class
    return GoogleNews(lang=language, period=period, start=start_time, end=end_time)

def google_search(language, period, start_time, end_time, search_term):
    """Receive a setted class and return the object with a search_term"""
    gn = set_google_news(language, period, start_time, end_time)
    gn.search(search_term)
    return gn

def get_page_results(language, period, start_time, end_time, search_term, n_times=10):
    """Iterate over the page results"""
    
    gn = google_search(language, period, start_time, end_time, search_term)
    # number of interactions
    n = 0
    # interate over the gn class
    while n <= n_times:
        try:
            data = gn.result()
            gn.getpage(n)
        except:
            pass
        n +=1
    return pd.DataFrame(data)

def parse_date(data, col_date='date'):
    """Returns a dataframe with a parsed date variable"""
    df = pd.DataFrame(data)
    print(df.shape)
    
    df['date'] = pd.to_datetime(df[col_date], errors='coerce')
    df.index = df.date
    return df

