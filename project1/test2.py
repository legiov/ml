import pandas as pd
import numpy as np
#from pandas.io.parsers import count_empty_vals


mb_data = pd.read_csv('~/pythonw/project1/data/melb_data.csv', sep=',');

#print(mb_data.head());

mb_df = mb_data.copy();

#print(mb_df.head())

mb_df = mb_df.drop(['index', 'Сoordinates'], axis=1)

#print(mb_df.head())
total_rooms = mb_df['Rooms'] + mb_df['Bedroom'] + mb_df['Bathroom']
mb_df['MeanRoomSquare'] = mb_df['BuildingArea']/total_rooms
#print(mb_df['MeanRoomSquare'])

diff_size = mb_df['BuildingArea'] - mb_df['Landsize']
sum_size = mb_df['BuildingArea'] + mb_df['Landsize']
mb_df['AreaRatio'] = diff_size/sum_size

#print(mb_df['AreaRatio'])

mb_df['Date'] = pd.to_datetime(mb_df['Date'])
#print(mb_df['Date'])
year_sold = mb_df['Date'].dt.year

#print(year_sold)
#print('min year: ', year_sold.min())
#print('max_year: ', year_sold.max())
#print('mode year: ', year_sold.mode()[0])
mb_df['MonthSale'] = mb_df['Date'].dt.month
#print(mb_df['MonthSale'].value_counts(normalize=True))

delta_days = mb_df['Date'] - pd.to_datetime('2016-01-01')
#print(delta_days)
mb_df['AgeBuilding'] = mb_df['Date'].dt.year - mb_df['YearBuilt']
#print(mb_df['AgeBuilding'])
mb_df = mb_df.drop('YearBuilt', axis=1)
mb_df['WeekdaySale'] = mb_df['Date'].dt.dayofweek
#print(mb_df[(mb_df['WeekdaySale']==5)|(mb_df['WeekdaySale']==6)].shape[0])

# На вход данной функции поступает строка с адресом.
def get_street_type(address):
# Создаём список географических пометок exclude_list.
    exclude_list = ['N', 'S', 'W', 'E']
# Метод split() разбивает строку на слова по пробелу.
# В результате получаем список слов в строке и заносим его в переменную address_list.
    address_list = address.split(' ')
# Обрезаем список, оставляя в нём только последний элемент,
# потенциальный подтип улицы, и заносим в переменную street_type.
    street_type = address_list[-1]
# Делаем проверку на то, что полученный подтип является географической пометкой.
# Для этого проверяем его на наличие в списке exclude_list.
    if street_type in exclude_list:
# Если переменная street_type является географической пометкой,
# переопределяем её на второй элемент с конца списка address_list.
        street_type = address_list[-2]
# Возвращаем переменную street_type, в которой хранится подтип улицы.
    return street_type

street_types = mb_df['Address'].apply(get_street_type)

popular_stypes = street_types.value_counts().nlargest(10).index

mb_df['StreetType'] = street_types.apply(lambda x: x if x in popular_stypes else 'other')

mb_df = mb_df.drop('Address', axis=1)

def get_weekend(weekday):
    return 1 if weekday > 4 else 0

mb_df['Weekend'] = mb_df['WeekdaySale'].apply(get_weekend)

#print(mb_df[mb_df['Weekend']==1]['Price'].mean())

popular_seller = mb_df['SellerG'].value_counts().nlargest(49).index

mb_df['SellerG'] = mb_df['SellerG'].apply(lambda x: x if x in popular_seller else 'other')

#print(mb_df[mb_df['SellerG']=='other'].shape[0])

nelson_min_price = mb_df[mb_df['SellerG']=='Nelson']['Price'].min()
other_min_price = mb_df[mb_df['SellerG']=='other']['Price'].min()

#print(nelson_min_price/other_min_price)

# создаём пустой список
unique_list = []

# пробегаемся по именам столбцов в таблице
for col in mb_df.columns:
    # создаём кортеж (имя столбца, число уникальных значений)
    item = (col, mb_df[col].nunique(), mb_df[col].dtype)
    # добавляем кортеж в список
    unique_list.append(item)

# создаём вспомогательную таблицу и сортируем её
unique_counts = pd.DataFrame(
    unique_list,
    columns=['Column_Name', 'Uniq_Count', 'Type']
).sort_values(by='Uniq_Count', ignore_index=True)

cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car'] # список столбцов, которые мы не берём во внимание
max_unique_count = 150 # задаём максимальное число уникальных категорий

for col in mb_df.columns:
    if mb_df[col].nunique() < max_unique_count and col not in cols_to_exclude:
        mb_df[col] = mb_df[col].astype('category')

#print(unique_counts)  
#print(mb_df.info())  
#print(mb_df['Regionname'].cat.categories)
#print(mb_df['Regionname'].cat.codes)
mb_df['Type'] = mb_df['Type'].cat.rename_categories({
    'u': 'unit',
    't': 'townhouse',
    'h': 'house'
})  

#print(mb_df['Type']) 
#mb_df['Type'] = mb_df['Type'].cat.add_categories('flat')
new_house_types = pd.Series(['unit', 'house', 'flat', 'flat', 'house'])
new_house_types = new_house_types.astype(mb_df['Type'].dtype)
#print(new_house_types)  

#print(mb_data.info()) 
uniq_suburb = mb_data['Suburb'].value_counts().nlargest(119).index

mb_df['Suburb'] = mb_df['Suburb'].apply(lambda x: x if x in uniq_suburb else 'other')
mb_df['Suburb'] = mb_df['Suburb'].astype('category')

#print(mb_df.info())
 
quater = mb_df['Date'].dt.quarter

#print(quater)

#mb_df['quarter'] = quater;
#print(mb_df['quarter'].value_counts())

#print(mb_df.sort_values(by='Price').head(10))
#print(mb_df.sort_values(by='Date', ascending=False).head(10))
#print(mb_df.sort_values(by=['Distance', 'Price']).loc[::10, ['Distance', 'Price']])
#mask1 = mb_df['AreaRatio'] < -0.8
#mask2 = mb_df['Type'] == 'townhouse'
#mask3 = mb_df['SellerG'] == 'McGrath'
#print(mb_df[mask1&mask2&mask3].sort_values(
#    by=['Date', 'AreaRatio'],
#    ascending=[True, False],
#    ignore_index=True).loc[:, ['Date', 'AreaRatio']])

#print(mb_df.sort_values(by='AreaRatio', ignore_index=True, ascending=False).loc[1558, 'BuildingArea'])

#mask1 = mb_df['Type'] == 'townhouse'
#mask2 = mb_df['Rooms'] > 2

#print(mb_df[mask1&mask2].sort_values(by=['Rooms', 'MeanRoomSquare'], ignore_index=True, ascending=[True, False])
#      .loc[18, 'Price'])

#print(mb_df.groupby(by='Type')['Price'].mean())

#print(mb_df.groupby(by='Regionname')['Distance'].min().sort_values(ascending=False))

#print(mb_df.groupby('MonthSale')['Price'].agg(['count', 'mean', 'max']).sort_values(by='count', ascending=False))

#print(mb_df.groupby('Regionname')['SellerG'].agg(['nunique', set]))

#print(mb_df.groupby('Rooms')['Price'].mean().max())

#print(mb_df.groupby('Regionname')['Lattitude'].std().min())

#print(mb_df[(mb_df['Date']>=pd.to_datetime('2017-05-01'))&(mb_df['Date']<=pd.to_datetime('2017-09-01'))]
#      .groupby('SellerG')['Price'].sum().min()
#      )

#print(mb_df.groupby('Rooms')[['Price', 'BuildingArea']].median());
#print(mb_df.groupby(['Rooms', 'Type'])['Price'].median().unstack())
#print(mb_df.pivot_table(values='Price', index='Rooms', columns='Type', fill_value=0).round(2))
#print(mb_df.pivot_table(columns='Weekend', index='Regionname', values='Price', aggfunc='count'))
#print(mb_df.pivot_table(values='Landsize', columns='Type', index='Regionname', aggfunc=['median', 'mean'], fill_value=0))
#print(mb_data.info())
#print(mb_df.pivot_table(values='Price', index=['Method', 'Type'], columns='Regionname', aggfunc='median', fill_value=0))
#pivot = mb_df.pivot_table(values='Landsize', index='Regionname', columns='Type', aggfunc=['median', 'mean'], fill_value=0)

#print(pivot.columns)
#print(pivot['mean']['unit'])
#mask  = pivot['mean']['house'] < pivot['median']['house']
#filtered_pivot = pivot[mask]
#print(filtered_pivot)
#print(mb_df.pivot_table(index='Rooms', columns='Type', values='BuildingArea', aggfunc='median'))
#print(mb_df.pivot_table(values='Price', index='SellerG', columns='Type', aggfunc='median')['unit'].max())