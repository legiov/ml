

import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.express as px


covid_df = pd.read_csv('~/pythonw/project1/data/covid/covid_data.csv')
vacc_df = pd.read_csv('~/pythonw/project1/data/covid/country_vaccinations.csv')
vacc_df = vacc_df[
    ['country', 'date', 'total_vaccinations', 
     'people_vaccinated', 'people_vaccinated_per_hundred',
     'people_fully_vaccinated', 'people_fully_vaccinated_per_hundred',
     'daily_vaccinations', 'vaccines']
]


covid_df = covid_df.groupby(['date', 'country'], as_index=False)[['confirmed', 'deaths', 'recovered']].sum();
covid_df['date'] = pd.to_datetime(covid_df['date'])
covid_df['active'] = covid_df['confirmed'] - covid_df['deaths'] - covid_df['recovered']
covid_df = covid_df.sort_values(['country', 'date'])
covid_df['daily_confirmed'] = covid_df.groupby('country')['confirmed'].diff()
covid_df['daily_deaths'] = covid_df.groupby('country')['deaths'].diff()
covid_df['daily_recovered'] = covid_df.groupby('country')['recovered'].diff()

vacc_df['date'] = pd.to_datetime(vacc_df['date'])
#print(covid_df.head())
#print(vacc_df.head())
#print(covid_df['date'].max())
result = covid_df.merge(vacc_df, how='left', on=['date', 'country'])
result['death_rate'] = result['deaths']/result['confirmed']*100
result['recovered_rate'] = result['recovered']/result['confirmed']*100
#print(result[result['country'] == 'United States']['death_rate'].max())
#print(result[result['country']=='Russia']['recovered_rate'].mean())
#grouped_cases = result.groupby('date')['daily_confirmed'].sum()
# grouped_cases.plot(
#     kind='line',
#     figsize=(12,4),
#     title="Ежедневная заболеваемость по всем странам",
#     grid=True,
#     lw=3
# )
# grouped_cases.plot(
#     kind='hist',
#     figsize=(10,6),
#     title="Распределение ежедневной заболеваемости",
#     grid=True,
#     color='green',
#     bins=10
# )

# grouped_country = covid_df.groupby('country')['confirmed'].last().nlargest(10)
# grouped_country.plot(
#     kind='bar',
#     grid=True,
#     figsize=(12,4),
#     colormap='plasma'
# )

# grouped_country = covid_df.groupby('country')[['confirmed','deaths']].last().nlargest(10, columns='confirmed')
# grouped_country.plot(
#     kind='bar',
#     grid=True,
#     figsize=(12,4)
# )

#result.groupby('country')['total_vaccinations'].last().nsmallest(5).plot(kind='bar')

# us_data = result[result['country']=='United States']

# fig = plt.figure(figsize=(8,4))
# axes = fig.add_axes([0, 0, 1, 1])
# axes.scatter(
#     x=us_data['people_fully_vaccinated'],
#     y=us_data['daily_confirmed'],
#     s=100,
#     marker='o',
#     c='blue'
# )

# vaccine_combinations = result['vaccines'].value_counts()[:10]
# fig = plt.figure(figsize=(5,5))
# axes = fig.add_axes([0,0,1,1])
# axes.pie(
#     vaccine_combinations,
#     labels=vaccine_combinations.index,
#     autopct='%.1f%%',
#     explode=[0.1, 0,0,0,0,0,0,0,0,0]
# )

# china_data = result[result['country']=='China']
# china_grouped = china_data.groupby(['date'])[['confirmed', 'active', 'deaths', 'recovered']].sum()

# #Визуализация
# fig = plt.figure(figsize=(10,4))
# axes = fig.add_axes([0,0,1,1])

# axes.plot(china_grouped['confirmed'], label='Общее число зафиксированных случаев', lw=3)
# axes.plot(china_grouped['deaths'], label='Общее число смертей', lw=3)
# axes.plot(china_grouped['recovered'], label='Общее число выздоровивших пациентов', lw=3)
# axes.plot(china_grouped['active'], label='Общее число активных случаев', lw=3, linestyle='dashed')

# #установка параметров отображения
# axes.set_title('Статистика ковид в Китае', fontsize=16)
# axes.set_xlabel('Даты')
# axes.set_ylabel('Число случаев')
# axes.set_yticks(range(0, 100000, 10000))
# axes.xaxis.set_tick_params(rotation=30)
# axes.grid()
# axes.legend()

# vacc_country = result.groupby('country')['people_fully_vaccinated'].last().nlargest(5)
# vacc_country_per_hundred = result.groupby('country')['people_fully_vaccinated_per_hundred'].last().nlargest(5)

# fig = plt.figure(figsize=(13,4))
# main_axes = fig.add_axes([0.1,0.1,0.9,0.9])
# main_axes.bar(
#     x=vacc_country.index,
#     height=vacc_country
# )
# main_axes.set_ylabel('Число вакцинированных (2 компонент)')
# main_axes.set_title('Топ 5 стран по вакцинированным 2 компонентом')

# insert_axes = fig.add_axes([0.6, 0.6, 0.3, 0.3])
# insert_axes.bar(x=vacc_country_per_hundred.index, height=vacc_country_per_hundred, width=0.5)
# insert_axes.set_ylabel('На 100 человек')
# insert_axes.xaxis.set_tick_params(rotation=45)

# russia_data = result[result['country']=='Russia']
# fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15,4))

# axes[0].bar(
#     x=russia_data['date'],
#     height=russia_data['daily_vaccinations'],
#     label='Число вакцинированных'
# )
# axes[0].set_title('Ежедневная вакцинация в России')
# axes[0].xaxis.set_tick_params(rotation=45)

# axes[1].plot(
#     russia_data['date'],
#     russia_data['daily_confirmed'],
#     label='Число заболевших',
#     color='tomato', lw=2
# )
# axes[1].set_title('Ежедневная заболеваемость в России')
# axes[1].xaxis.set_tick_params(rotation=45)

# axes[2].hist(
#     x=russia_data['daily_confirmed'],
#     label='Число заболевших',
#     color='lime', bins=20
# )
# axes[2].set_title('Гистограмма заболеваемости в России')
# axes[2].xaxis.set_tick_params(rotation=30)

# ----------------- Seaborn----------------------
# print(sns.__version__)
coutries = ['Russia', 'Australia', 'Germany', 'Canada', 'United Kingdom'];
grouped_covid_df = result[result['country'].isin(coutries)]

populations = pd.DataFrame([
    ['Canada', 37664517],
    ['Germany', 83721496],
    ['Russia', 145975300],
    ['Australia', 25726900],
    ['United Kingdom', 67802690]
    ],
    columns=['country', 'population']
)
grouped_covid_df = grouped_covid_df.merge(populations, on=['country'])
grouped_covid_df['daily_confirmed_per_hundred'] = grouped_covid_df['daily_confirmed'] / grouped_covid_df['population']*100
#print(grouped_covid_df['daily_confirmed_per_hundred'].head(20))

# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10,8))
# sns.histplot(
#     data=grouped_covid_df,
#     x='daily_confirmed_per_hundred',
#     bins=25,
#     kde=True,
#     ax=axes[0]
# )
# sns.histplot(
#     data=grouped_covid_df,
#     x='daily_confirmed_per_hundred',
#     y='country',
#     bins=25,
#     color='red',
#     ax=axes[1]
# )

# fig = plt.figure(figsize=(10,7))
# boxplot = sns.boxplot(
#     data=grouped_covid_df,
#     y='country',
#     x='death_rate',
#     orient='h',
#     width=0.9
# )

# boxplot.set_title('Распределение летальности по странам')
# boxplot.set_xlabel('Летальность')
# boxplot.set_ylabel('Страна')
# boxplot.grid()

# fig = plt.figure(figsize=(10,7))
# grouped_covid_df['quarter'] = grouped_covid_df['date'].dt.quarter

# barplot = sns.barplot(
#     data=grouped_covid_df,
#     x='country',
#     y='daily_confirmed_per_hundred',
#     hue='quarter'
# )
# barplot.set_title('Средний процент болеющего населения по кварталам')

# joinplot = sns.jointplot(
#     data=grouped_covid_df,
#     x='people_fully_vaccinated_per_hundred',
#     y='daily_confirmed_per_hundred',
#     hue='country',
#     xlim=(0,40),
#     ylim=(0, 0.1),
#     height=8
# )

# pivot = grouped_covid_df.pivot_table(
#     values='people_vaccinated_per_hundred',
#     columns='date',
#     index='country'
# )
# pivot.columns = pivot.columns.astype('string')

# heatmap = sns.heatmap(data=pivot, cmap='YlGnBu')
# heatmap.set_title('Тепловая карта вакцинации', fontsize=16)

# grouped_covid_df['confirmed_per_hundred'] = grouped_covid_df['confirmed']/grouped_covid_df['population']*100
# pivot = grouped_covid_df.pivot_table(
#     values='confirmed_per_hundred',
#     columns='date',
#     index='country'
# )
# pivot.columns = pivot.columns.astype('string')
# heatmap = sns.heatmap(
#     data=pivot,
#     cmap='YlGnBu'
# )
#grouped_covid_df.info()
# box = sns.boxplot(
#     data=grouped_covid_df,
#     x='country',
#     y='recovered_rate',
#     width=0.9
# )


#---------------------------Plotly-----------------------------
#print(plotly.__version__)

# line_data = result.groupby('date', as_index=False).sum()
# fig = px.line(
#     data_frame=line_data,
#     x='date',
#     y=['confirmed', 'recovered', 'deaths', 'active'],
#     height=500,
#     width=1000,
#     title='Данные'
# )

# bar_data = result.groupby('country', as_index=False)['recovered_rate'].mean().nlargest(10, columns=['recovered_rate'])
# fig = px.bar(
#     data_frame=bar_data,
#     x='country',
#     y='recovered_rate',
#     color='country',
#     text='recovered_rate',
#     orientation='v',
#     height=500,
#     width=1000,
#     title='recov rate'
# )
# result.info()
# tree_data = result.groupby('country', as_index=False)[['daily_recovered']].mean()
# # tree_data.info()
# fig = px.treemap(
#     data_frame=tree_data,
#     path=['country'],
#     values='daily_recovered',
#     height=500,
#     width=1000,
#     title='daily recovered'
# )

# choropleth_data = result.sort_values(by='date')
# choropleth_data['date'] = choropleth_data['date'].astype('string')
# fig = px.choropleth(
#     data_frame=choropleth_data,
#     locations='country',
#     locationmode='country names',
#     color='confirmed',
#     animation_frame='date',
#     range_color=[0, 30e6],
#     title='Global Spread of Covid',
#     width=800,
#     height=500,
#     color_continuous_scale='Reds'
# )

# countries=['United States', 'Russia', 'United Kingdom', 'Brazil', 'France']
# scatter_data = result[result['country'].isin(coutries)]

# fig = px.scatter_3d(
#     data_frame=scatter_data,
#     x='daily_confirmed',
#     y='daily_deaths',
#     z='daily_vaccinations',
#     color='country',
#     log_x=True,
#     log_y=True,
#     width=1000,
#     height=700
# )

# data = result.groupby('date', as_index=False)['daily_vaccinations'].sum()

# fig  = px.line(
#     data_frame=data,
#     x='date',
#     y='daily_vaccinations',
#     height=500,
#     width=500
# )
coutries = ['United States', 'Russia', 'United Kingdom', 'Brazil', 'France', 'Japan'];
data = result[result['country'].isin(coutries)]
data = data[data['date'] == pd.to_datetime('2021-03-24')]
data = data
#data.columns = data.columns.astype('string')
print(data.head(10))
# print(data.head(10))
fig = px.density_heatmap(
    data_frame=data,
    x='date',
    y='country',
    z='total_vaccinations'
)
fig.show()
