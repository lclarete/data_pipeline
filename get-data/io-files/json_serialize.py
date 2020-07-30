# serializes one or several JSON files

from fileinput import FileInput
import json


def load_json_multiple(segments):
    chunk = ""
    for segment in segments:
        chunk += segment
        try:
            yield json.loads(chunk)
            chunk = ""
        except ValueError:
            pass
        

# serialize JSON to Python  
def serialize_json(file_path):
    tweet_list = []
    # reading one single file
    if type(file_path) == str:        
        # open file with FileInput
        with open(file_path) as file:
            for line in load_json_multiple(file):
                tweet_list.append(line)
        # close the file
        file.close()
    # reading a list of files
    if type(file_path) == list:
        for each_file in file_path:
            with open(each_file) as file:
                for line in load_json_multiple(file):
                    tweet_list.append(line)
    return(tweet_list)




# merge JSON files into a single one

import json

# serialize JSON to Python  
def merge_json(list_files_path):
    files_to_be_merged = serialize_json(list_files_path)
    with open('merged_json.json', 'w') as write_file:
        json.dump(files_to_be_merged, write_file, indent=4)
    return(files_to_be_merged)



import pandas as pd

# transform a listo into a dataframe
def df_tweet(tweet_list):
    # extract columns and return a dataframe
    data_df = pd.DataFrame([{
        # tweet data
        "tweet_created_at": x['created_at'],
        "tweet_id": x['id'],
        "tweet_text": x['text'],
        "tweet_retweet_count": x['retweet_count'],
        "tweet_quote_count": x['quote_count'],
        "tweet_reply_count": x['reply_count'],
        "tweet_favorite_count": x['favorite_count'],
        "tweet_hashtags": x['entities']['hashtags'],
        "tweet_urls": x['entities']['urls'],
        "tweet_user_mentions": x['entities']['user_mentions'],

        # tweet's user dar
        "user_name": x['user']['name'],
        "user_screen_name": x['user']['screen_name'],
        "user_location": x['user']['location'] if 'location' in str(x) else None,
        "tweet_user_coordinates": x['coordinates'] if 'coordinates' in str(x) else None,    
        "user_followers_count": x['user']['followers_count'],
        "user_friends_count": x['user']['friends_count'],
        "user_favourites_count": x['user']['favourites_count'],
        "user_statuses_count": x['user']['statuses_count'],
        "user_date_profile_creating": x['user']['created_at'],
        "user_verified_account": x['user']['verified'],

        # retweeted data
        "rt_created_at": x['retweeted_status']['created_at'] if 'retweeted_status' in x else None,
        "rt_id": x['retweeted_status']['id'] if 'retweeted_status' in x else None,
        "rt_in_reply_to_status_id": x['retweeted_status']['in_reply_to_status_id'] if 'retweeted_status' in x else None,
        "rt_retweet_count": x['retweeted_status']['retweet_count'] if 'retweeted_status' in x else None,
        "rt_favorite_count": x['retweeted_status']['favorite_count'] if 'retweeted_status' in x else None,
        "rt_reply_count": x['retweeted_status']['reply_count'] if 'retweeted_status' in x else None,
        "rt_quote_count": x['retweeted_status']['quote_count'] if 'retweeted_status' in x else None,
        "rt_in_reply_to_screen_name": x['retweeted_status']['in_reply_to_screen_name'] if 'full_text' in x else None,
        "rt_hashtags": x['retweeted_status']['extended_tweet']['entities']['hashtags'] if 'full_text' in x else None,
        "rt_urls": x['retweeted_status']['extended_tweet']['entities']['urls'] if 'full_text' in x else None,
        "rt_user_mentions": x['retweeted_status']['extended_tweet']['entities']['user_mentions'] if 'full_text' in x else None,
        "rt_symbols": x['retweeted_status']['extended_tweet']['entities']['symbols'] if 'full_text' in x else None,

        # retweeted: with more than 140 characteres
        "rt_extended_tweet_full_text": x['retweeted_status']['extended_tweet']['full_text'] if 'full_text' in x else None,    

        # quoted tweet
        "rt_user_name": x['retweeted_status']['user']['name'] if 'retweeted_status' in x else None,
        "rt_user_screen_name": x['retweeted_status']['user']['screen_name'] if 'retweeted_status' in x else None,
        "rt_user_followers_count": x['retweeted_status']['user']['followers_count'] if 'retweeted_status' in x else None,
        "rt_user_friends_count": x['retweeted_status']['user']['friends_count'] if 'retweeted_status' in x else None,
        "rt_user_favourites_count": x['retweeted_status']['user']['screen_name'] if 'retweeted_status' in x else None,
        "rt_user_statuses_count": x['retweeted_status']['user']['favourites_count'] if 'retweeted_status' in x else None,
        "rt_user_screen_name": x['retweeted_status']['user']['screen_name'] if 'retweeted_status' in x else None,    

    } for x in tweet_list])#.set_index("tweet_created_at")
    return(data_df)