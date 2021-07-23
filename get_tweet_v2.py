import tweepy
import os
from replit import db
import datetime

def retrieve_last_seen_id(username: str, ids = None):
    value = db[username].value

    if value == []:
        store_last_seen_id(ids, username)
    else:
        last_seen_id = int(value[-1])
        return last_seen_id

def retrieve_last_seen_date(username: str, date = None):
    value = db[username]

    if len(value) == 0:
        store_last_seen_date(date, username)
    else:
        last_seen_date = value
        return last_seen_date

def store_last_seen_id(last_seen_id, username: str):
    value = db[username]
    value.append(str(last_seen_id))
    db[username] = value

    return

def store_last_seen_date(last_seen_date, username: str):
    value = db[username]
    value = str(last_seen_date)
    db[username] = value

    return

def get_tweet_id_old(username: str):

    CONSUMER_KEY = os.environ["CONSUMER_KEY"]
    CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
    ACCESS_KEY = os.environ["ACCESS_KEY"]
    ACCESS_SECRET = os.environ["ACCESS_SECRET"]

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    API = tweepy.API(auth)

    username = username.strip("@")
    timelines = API.user_timeline(username, count = 1)
    if len(timelines) == 0:
      return None, username
    retrieve_last_seen_id(username, timelines[0].id)

    if timelines[0].id != retrieve_last_seen_id(username):
        store_last_seen_id(timelines[0].id, username)
        return timelines[0].id, username
    else:
        return None, username

def get_tweet_id(username: str):

    CONSUMER_KEY = os.environ["CONSUMER_KEY"]
    CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
    ACCESS_KEY = os.environ["ACCESS_KEY"]
    ACCESS_SECRET = os.environ["ACCESS_SECRET"]

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    API = tweepy.API(auth)

    username = username.strip("@")
    timelines = API.user_timeline(username, count = 1)
    if len(timelines) == 0:
      return None, username
    retrieve_last_seen_date(username, timelines[0].created_at)

    if timelines[0].created_at > datetime.datetime.strptime(retrieve_last_seen_date(username), "%Y-%m-%d %H:%M:%S"):
        store_last_seen_date(timelines[0].created_at, username)
        return timelines[0].id, username
    else:
        return None, username

if __name__ == "__main__":
    print(get_tweet_id("TZGyn"))