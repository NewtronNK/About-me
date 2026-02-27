import pandas as pd
import requests

df = pd.read_csv('netflix_titles.csv')

API_KEY = '8b7c8c4'
df['IMDb rating'] = None
df['language'] = None

df.loc[df['rating'] == '74 min', 'rating'] = 'TV-MA'
df.loc[df['rating'] == '74 min', 'duration'] = '74 min'

df.loc[df['rating'] == '84 min', 'rating'] = 'TV-MA'
df.loc[df['rating'] == '84 min', 'duration'] = '84 min'

df.loc[df['rating'] == '66 min', 'rating'] = 'TV-MA'
df.loc[df['rating'] == '66 min', 'duration'] = '66 min'

for i in range(len(df)):
    movie_title = df['title'].iloc[i].replace(' ', '+')
    movie_year = df['release_year'].iloc[i]
    movie_country = df['country'].iloc[i]
    url = f"http://www.omdbapi.com/?t={movie_title}&y={movie_year}&plot=full&apikey={API_KEY}"

    response = requests.get(url)

    # ตรวจสอบการตอบกลับ
    if response.status_code == 200:
        data = response.json()
        if data['Response'] == 'True':
          df.at[i, 'IMDb rating'] = data['imdbRating']
          df.at[i, 'language'] = data['Language']
          if pd.isnull(df.at[i, 'director']):
            df.at[i, 'director'] = data["Director"]
          if pd.isnull(df.at[i, 'cast']):
            df.at[i, 'cast'] = data["Actors"]
          if pd.isnull(df.at[i, 'country']):
            df.at[i, 'country'] = data["Country"]

df.replace('NaN', 'None', inplace=True)
df.replace('N/A', 'None', inplace=True)
df.fillna(value='None', inplace=True)
df.to_csv('netflix_titles.csv', index=False)