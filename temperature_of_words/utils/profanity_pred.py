import tweepy as tw
from requests_oauthlib import OAuth1Session
import datetime
import re
import numpy as np
import pandas as pd
from utils.d_pre import tokenize, make_features, make_features2

# basic settigns for tweepy
api_key = 'MslsWzWgIGUPNc2iLHM3Kbmyi'
api_secret_key = '2F91OX4ZEj8YnxjEURvaxI6ACPnjm1h0TCDreRxYkiapgTyeW3'
access_token = '1372444419073351682-Cwh5Pzh8nC8YzxHGDiOK5MAuHjByx7'
access_token_secret = '1fwg8XaNDCtTaT1yLwolRFaQzluhb6EHt7ZJGrs4AlrWN'


twitter = OAuth1Session(api_key,
                        client_secret=api_secret_key,
                        resource_owner_key=access_token,
                        resource_owner_secret=access_token_secret)
auth = tw.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


def get_tweet_text(search_word, search_cnt=10):
    search_words = search_word
    search_cnt = search_cnt

    # setting datetime
    today = datetime.datetime.now()
    today = today.replace(hour=23, minute=59, second=59, microsecond=999999)
    yesterday = today - datetime.timedelta(1)

    tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang="en",
                       tweet_mode='extended',
                       until=today.date()
                       ).items(search_cnt)

    tweets_list = []

    for tweet in tweets:
        if yesterday.date() == tweet.created_at.date():
            if 'retweeted_status' in tweet._json:
                full_text = tweet._json['retweeted_status']['full_text']
            else:
                full_text = tweet.full_text

            tweets_list.append(re.sub(r'@[A-Za-z0-9]*', '', full_text).strip())

    return tweets_list


def text_processing(lst):

    rst = pd.DataFrame(np.array(lst)).rename(columns={0: 'text'})
    # tokenized df
    t_df = tokenize(rst)

    f1_df = make_features(rst)
    f2_df = make_features2(t_df)

    return pd.concat([f1_df, f2_df], axis=1)
