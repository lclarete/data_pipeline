from apiclient.discovery import build
import pandas as pd
from datetime import datetime

"""
- title
- description
- views
- likes
- dislikes
- comments
- author
- link
"""

API_KEY = "YOUR API KEY"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}

# variables
START_DATE = "Jan 13, 2021"
END_DATE = "Oct 15, 2021"
KEYWORD = "avengers"
REQUEST_COUNT = 4 #Each request returns 50 videos

def textToDate(string):
    date = datetime.strptime(string, "%b %d, %Y")
    return date

def dateToTime(date):
    time = date.strftime("%Y-%m-%dT%H:%M:%SZ")
    return time

def createResponse(start, end):
    req = youtube.search().list(
        q=KEYWORD,
        part="snippet",
        type="video",
        maxResults=50, 
        publishedAfter=start, 
        publishedBefore=end
    )
    
    return req

def videoStats(url):
    req = youtube.videos().list(
        id=url,
        part="statistics"
    )

    return req

start = textToDate(START_DATE)
end = textToDate(END_DATE)

youtube = build("youtube", "v3", developerKey=API_KEY)

quarter = (end-start)/REQUEST_COUNT
local_start = start
local_end = start+quarter

big_data_list = []
for _ in range(REQUEST_COUNT):
    publishedAfter = dateToTime(local_start)
    publishedBefore = dateToTime(local_end)
    req = createResponse(publishedAfter, publishedBefore)
    res = req.execute()
    items = res.get("items", [])

    ids = []
    data_list = []
    for i in range(len(items)):
        data = {}
        channelName = items[i]["snippet"]["channelTitle"]
        title = items[i]["snippet"]["title"]
        description = items[i]["snippet"]["description"]
        videoId = items[i]["id"]["videoId"]
        url = "https://www.youtube.com/watch?v=" + videoId
        data["channelName"] = channelName
        data["title"] = title
        data["description"] = description
        data["url"] = url

        ids.append(videoId)
        data_list.append(data)

    urlString = ",".join(ids)
    statsReq = videoStats(urlString)
    statsRes = statsReq.execute()
    statsItems = statsRes.get("items", [])

    stats_list = []
    for i in range(len(statsItems)):
        stats = {}
        viewCount = statsItems[i]["statistics"].get("viewCount", "N/A")
        likeCount = statsItems[i]["statistics"].get("likeCount", "N/A")
        dislikeCount = statsItems[i]["statistics"].get("dislikeCount", "N/A")
        commentCount = statsItems[i]["statistics"].get("commentCount", "N/A")

        stats["viewCount"] = viewCount
        stats["likeCount"] = likeCount
        stats["dislikeCount"] = dislikeCount
        stats["commentCount"] = commentCount

        stats_list.append(stats)

    assert len(stats_list) == len(data_list), "stats and data are not of same length"
    
    for i in range(len(stats_list)):
        data = data_list[i]
        stats = stats_list[i]
        
        total = {**data, **stats}
        big_data_list.append(total)

    local_start = local_end
    local_end += quarter


df = pd.DataFrame(big_data_list)
json_name = KEYWORD+".json"
df.to_json(json_name, orient="records", indent=4)