"""
Connect YouTube API.

### More about YouTube API
* Get all videos from a channel: https://github.com/nikhilkumarsingh/YouTubeAPI-Examples/blob/master/4.Channel-Vids.ipynb

* Get most disliked videos from a channel: https://github.com/nikhilkumarsingh/YouTubeAPI-Examples/blob/master/5.Most-Disliked-Channel-Vids.ipynb


"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# flatten json data
from pandas.io.json import json_normalize

from datetime import datetime


# https://developers.google.com/youtube/v3/docs/search/list
from apiclient.discovery import build
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
DEVELOPER_KEY = "AIzaSyBKhbu3j5izgiPqBALUedXHtSqeGrPXM9o"

# connect to youtube api and returns videos
def youtube_search(q, max_results=50, 
                   order="viewCount", 
                   pageToken=None, 
                   location=None, 
                   publishedAfter=None,
                   publishedBefore=None):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=q,
        type="video",
        pageToken=pageToken,
        order = order,
        part="id,snippet",
        maxResults=max_results,
        location=location,
        publishedAfter=publishedAfter,
        publishedBefore=publishedBefore
    ).execute()
    return(search_response)


# read json and return a dataframe using values from output json data
cols = ['kind', 'etag', 'id', 'publishedAt', 'channelId', 'title', 'description', 'channelTitle','liveBroadcastContent', 'thumbnails.default.url']

def json_to_dataframe(res_json, cols=cols):
    df = pd.DataFrame(res_json['items'])
    df['id'] = json_normalize(df.id).videoId
    df_videos = json_normalize(df.snippet)
    df_final = pd.concat([df, df_videos], axis=1)
    df_final = df_final[cols]
    df_final['date'] = pd.to_datetime(df_final.publishedAt)
    df_final.index = df_final.date
    df_final.sort_index(inplace=True)
    return(df_final)

## Defining global variables and calling youtube search function
query_asma = 'asma AND chiado OR chia OR dor OR peito OR tosse* OR remedio OR doença* OR saúde OR crise* OR sintoma* OR morte* OR morre* OR trata* OR ter OR cuida* OR adulto* OR criança* OR bronquite* OR simpatia* OR hospital OR diagnost* OR benz*)'
query_esquizo = 'esquizofren* , brazil'
query_depre = 'depressão'
# topic_health = '/m/0kt51'

# start_time = datetime(year=2018, month=7, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')
# end_time = datetime(year=2018, month=9, day=30).strftime('%Y-%m-%dT%H:%M:%SZ')

def n_youtube(query, year_post):
    string_time = '%Y-%m-%dT%H:%M:%SZ'
    dfs = []
    n = 0
    for i in range(1, 13):
        n +=1
        if n == 2:
            start_time = datetime(year=year_post, month=n, day=1).strftime(string_time)
            end_time = datetime(year=year_post, month=n, day=28).strftime(string_time)
            dfs.append([n, youtube_search(q=query, publishedAfter=start_time, publishedBefore=end_time)])
        elif n in [1, 3, 5, 7, 8, 10, 12]:
            start_time = datetime(year=year_post, month=n, day=1).strftime(string_time)
            end_time = datetime(year=year_post, month=n, day=31).strftime(string_time)
            dfs.append([n, youtube_search(q=query, publishedAfter=start_time, publishedBefore=end_time)])
        else:
            start_time = datetime(year=year_post, month=n, day=1).strftime(string_time)
            end_time = datetime(year=year_post, month=n, day=30).strftime(string_time)
            dfs.append([n, youtube_search(q=query, publishedAfter=start_time, publishedBefore=end_time)])
    df = json_normalize(pd.DataFrame(dfs)[1])
    return(df)

def video_items(df, n=12):
    videos = []
    for i in range(0, n):
        videos.append(json_normalize(df['items'][i]))
    df_videos = pd.concat(videos)
    df_videos['date'] = pd.to_datetime(df_videos['snippet.publishedAt'])
    df_videos['year'] = df_videos.date.dt.year
    df_videos['month'] = df_videos.date.dt.month
    return(df_videos)

def youtube_total(query, year):
    df = n_youtube(query, year)
    df['year'] = year
    df['month'] = df.index + 1
    df_videos = video_items(df)
    return(df, df_videos)