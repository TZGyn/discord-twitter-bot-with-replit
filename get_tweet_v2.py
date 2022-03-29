import datetime
import os

import tweepy
from replit import db


def retrieve_last_seen_date(username: str, date = None):
    value = db[username]

    if len(value) == 0:
        store_last_seen_date(date, username)
    else:
        last_seen_date = value
        return last_seen_date

def store_last_seen_date(last_seen_date, username: str):
    value = db[username]
    value = str(last_seen_date)
    db[username] = value

    return

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
    print(get_tweet_id(""))
