import pandas as pd

df1 = pd.read_csv('~/Documents/Project-Netflix/netflix_titles_copy.csv')
df2 = pd.read_csv('~/Documents/Project-Netflix/netflix_titles_updating.csv')
print("current null count ",df1['director'].isna().sum())
print("originaly has ",df2['director'].isna().sum())
print("None coutn == ",df1['director'].str.count("None").sum())
