import pandas as pd
import re
import numpy as np 

movies = pd.read_csv('~/pythonw/project1/data/movies/movies.csv', sep=',')
dates = pd.read_csv('~/pythonw/project1/data/movies/dates.csv', sep=',')
ratings1 = pd.read_csv('~/pythonw/project1/data/movies/ratings1.csv', sep=',')
ratings2 = pd.read_csv('~/pythonw/project1/data/movies/ratings2.csv', sep=',')

#movies.info()
#print(ratings1.nunique())
year = pd.to_datetime(dates['date'])
year = year.dt.year
#print(year.value_counts().max())
#print(dates.head(5))
ratings = pd.concat([ratings1, ratings2], ignore_index=True)
#ratings.info()
ratings = ratings.drop_duplicates(ignore_index=True)
ratings = pd.concat([ratings, dates], axis=1)
#print(ratings.tail(5))
joined_false = ratings.join(movies.set_index('movieId'), on='movieId', how='left')

#print(joined_false)
merged = ratings.merge(movies, on='movieId', how='left')
print(merged)



def get_year_release(arg):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', arg) 
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	   #очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем None
        return None

merged['year_release'] = merged['title'].apply(get_year_release)
merged['year_release'] = merged['year_release'].astype(int, errors='ignore')
#merged['year_release'].dtype = np.int64
merged['year_rating'] = pd.to_datetime(merged['date']).dt.year
print(merged)

#print(merged[merged['year_release'] == 2010].groupby('genres')['rating'].mean().sort_values())
#print(merged.groupby('userId')['genres'].nunique().sort_values())
#print(merged.groupby('userId')['rating'].agg(['count','mean']).sort_values(['count','mean'], ascending=[True, False]))
#mask = merged['year_release']==2018
#print(merged[mask].groupby('genres')['rating'].agg(['count', 'mean']))
pivot = merged.pivot_table(columns='year_rating', index='genres', values='rating', fill_value=0)

print(pivot)
#print(pivot.loc[:,2018].sort_values())
print(pivot.loc['Comedy'])