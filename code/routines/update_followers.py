import pandas as pd
from datetime import date
from collections import ChainMap
from twitter_scraper import fetch_number_of_followers

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

filepath = './data/dep_followers.csv'
deputies = pd.read_csv(filepath)

filepath_accounts = './data/dep_description.csv'
accounts = pd.read_csv(filepath_accounts)
accounts = accounts[['id_dep', 'twitter_account']]

screen_names = accounts.twitter_account[accounts['twitter_account'] != 'no-twitter'].tolist()

number_of_followers = fetch_number_of_followers(screen_names)
followers_dict = dict(ChainMap(*number_of_followers))

# breakpoint()

accounts['date'] = date.today().strftime("%d/%m/%Y")
accounts['followers'] = accounts['twitter_account'].map(followers_dict)

deputies = deputies.append(accounts, ignore_index=True)
# print(deputies.to_markdown())

deputies.to_csv("./data/dep_followers.csv", encoding='utf-8', index=False)
