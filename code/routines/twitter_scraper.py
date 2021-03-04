import os
import csv
import time
import tweepy
from datetime import date
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

def fetch_friends_list(user_screen_name):

    api = tweepy.API(auth, wait_on_rate_limit=True)

    twitter_user = api.get_user(user_screen_name)

    print(f'Scrapping {twitter_user.screen_name}...')

    users = []
    for page in tweepy.Cursor(api.friends, screen_name=user_screen_name).pages():
        users.extend(page)
        time.sleep(5)

    print(f"Username is following {len(users)} users")

    names = [user.name for user in users]
    screen_names = [user.screen_name for user in users]

    headers = ['name', 'screen_name']
    rows = zip(names, screen_names)

    # import ipdb; ipdb.set_trace()

    with open("../data/dep_names_and_screen_names.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)
        for row in rows:
            csvwriter.writerow(row)


def fetch_number_of_followers(list_of_users):

    print("getting the number of followers from:")

    api = tweepy.API(auth, wait_on_rate_limit=True)

    followers_dict = []

    for user in list_of_users:
        try:
            account = api.get_user(user)
            print(f"Scrapping @{account.screen_name}...")
            followers_dict.append({ account.screen_name : account.followers_count })
        except:
            print(f"{user}'s account not found")

    return followers_dict
