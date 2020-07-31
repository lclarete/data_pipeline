"""
Public Twitter API
retrieve a sample (approximately 1%) of all Twitters
that are currently being published by users.

A. Make sure you understand the rules and
purpose of the different APIs:

https://developer.twitter.com/en/docs

https://developer.twitter.com/en/developer-terms/policy

https://brightplanet.com/2013/06/25/twitter-firehose-vs-twitter-api-whats-the-difference-and-why-should-you-care/


B. Before running this file, make sure you have the TWITTER exported variable

1. Create a directory with the name twitter-files
2. Create a file called credentials.txt with the twitter credentials:
app_key=YOUR CONSUMER KEY  
app_secret=YOUR CONSUMER SECRET  
oauth_token=YOUR ACCESS TOKEN  
oauth_token_secret=YOUR ACCESS TOKEN SECRET
3. Export a TWITTER variable on your unix-like system
$ export TWITTER='path/to/your/twitter-files

C. NLTK Twitter lib uses Twython package to perform the data collection
1. Install Twython


"""

from nltk.twitter import Twitter, Query, Streamer, Twitter, TweetViewer, TweetWriter, credsfromfile

# PARAMETERS

# keywords
keywords = 'sexo, trepar, foder'

# number of max tweets
limit=5

# ff True, print the files in the screen
# if False, salve the tweets in a json file
to_screen=False

# if True, retrieve live tweets
# if False, retrieve past tweets
stream=False


################### --- Twitter Class --- ###################
# tw = Twitter()
# tw.tweets(keywords=keywords, limit=limit, to_screen=to_screen, stream=stream)



################### --- Credsfromfile --- ###################
# Define the credentials
oauth = credsfromfile()


################### --- Streamer Class --- ###################
# Define a client using Streamer API
# client = Streamer(**oauth)

# register with TweetViewer() instead of TweetWriter()
# client.register(TweetViewer(limit=limit))

# return a sample of tweets, without any filter
# client.sample()

# client.filter(track='bolsonaro')


################### --- Query class --- ###################
client = Query(**oauth)

# instead of viewing the tweets, write it down
client.register(TweetWriter())

# define the users to retrieve the data
client.user_tweets('RealDonaldTrump', 10)

# only accepts one keyword as an argument
tweets = client.search_tweets(keywords='nltk', limit=10)

tweet = next(tweets)

from pprint import pprint
pprint(tweet, depth=1)
