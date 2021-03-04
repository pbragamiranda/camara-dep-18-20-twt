import pandas as pd
import numpy as np
from helpers import daily_diff

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

filepath = './data/dep_followers.csv'

deputies = pd.read_csv(filepath)


# print(deputies.to_markdown())

df = pd.pivot_table(deputies, index=['name', 'screen_name'], columns=['date'])

df.columns = df.columns.droplevel()
df.reset_index(level=0, inplace=True)
df.reset_index(level=0, inplace=True)
df.columns.name = 'id'


df['diff-23-22'] = daily_diff(df['23/02/2021'], df['22/02/2021'])
df['diff-24-23'] = daily_diff(df['24/02/2021'], df['23/02/2021'])

# breakpoint()

# print(df.sort_values(by='diff-24-23', ascending=False).to_markdown())
print(df.sort_values(by='24/02/2021', ascending=False).to_markdown())

