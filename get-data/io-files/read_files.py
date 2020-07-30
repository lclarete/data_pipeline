# dataset
import pandas as pd
import numpy as np
import json

# import files
import glob2


# viz
import matplotlib as plt
import seaborn as sns
from matplotlib import rcParams

# df = pd.concat(map(pd.read_csv, ['data/d1.csv', 'data/d2.csv','data/d3.csv']))

# from os import listdir 
# filepaths = [f for f in listdir("./data") if f.endswith('.csv')] df = pd.concat(map(pd.read_csv, filepaths))

# import glob, os 
# df = pd.concat(map(pd.read_csv, glob.glob(os.path.join('', "my_files*.csv"))))

# import dask.dataframe as dd 
# df = dd.read_csv('data*.csv')


# read multiple CSV files
def read_multiple_json(files_path, lines=True):
    '''Read multiple json files. If lines=True, reads a multiline file as default'''

    # improvements: quit the / after the string file
    # if files_path.endswith('/'):
        # files_path = files_path[]

    # create a file path that consider the JSON's
    files_path = files_path + '/*/*.json'

    # get the multiple file paths using glob2 lib
    json_files = glob2.glob(files_path)
    
    # read the files using pandas and stores it in a list
    # as it is a multiple line JSON, lines=True
    l = [pd.read_json(file, lines=lines) for file in json_files]

    # returns the concated list in a dataframe format
    return pd.concat(l)


# read multiple CSV files
def read_multiple_csv(files_path, lines=True):
    '''Read multiple csv files. If lines=True, reads a multiline file as default'''

    # create a file path that consider the JSON's
    files_path = files_path + '/**/*.csv'

    # get the multiple file paths using glob2 lib
    csv_files = glob2.glob(files_path)
    
    # read the files using pandas and stores it in a list
    l = [pd.read_csv(file) for file in csv_files]

    # returns the concated list in a dataframe format
    return pd.concat(l)


def read_one_json_file(path):
    '''Read just one json file with open json loads'''
    l = []
    with open(path) as f:
        for jsonObj in f:
            d = json.loads(jsonObj)
            
            # replace break lines
            d['tweet'] = d['tweet'].replace('\r', ' ').replace('\n', ' ')
            l.append(d)
    return l


def read_several_json_files(files_path):
    '''Read several json files with open'''
    files_path = files_path + '**/*.json'
    json_files = glob2.glob(files_path)
    list_json_files = []
    for file in json_files:
        list_json_files.append(pd.DataFrame(read_one_json_file(file)))
    return pd.concat(list_json_files)


def json_to_csv(path, file_name):
    '''Join and export a json to a csv file'''
    df = read_several_json_files(path)
    df.to_csv('/Users/liviaclarete/coding/corruption_article/data/clean/'+ file_name + '.csv', index=False)

# define the columns to be read
cols = ['id', 'date', 'time', 'likes_count', 'replies_count', 'retweets_count', 'tweet', 'conversation_id']


# -------------------------------------------
# type of each considered variable
dtypes = {
'id': object,
'date':object,
'time':object,
'likes_count':float,
'replies_count':float,
'retweets_count':float}
    
def read_csv_twitter(path, cols=cols, dtypes=dtypes):
    """
    Read csv data using dtype, usecols and 
    parse_dates parameters

    Return year, month and month_year variables
    
    """

    # call the read_csv function with all the parameters
    df = pd.read_csv(path, 
                    usecols=cols, 
                    dtype=dtypes,
                    parse_dates=['date', 'time']
                    )
    
    # create the date variables
    df['year'] = df.date.dt.year
    df['month'] = df.date.dt.month_name()
    df['month_year'] = df.date.dt.to_period('M')
    
    return df


def resample_period(df, period):
    """Use Y for year, M for month and D for day"""
    table = df.resample(period)['id'].count().reset_index() 
    table[period] = table.date.dt.to_period(period)
    table = pd.concat([table[period], table.id], axis=1)
    return table