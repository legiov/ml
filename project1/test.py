import pandas as pd

melb_data = pd.read_csv('~/pythonw/project1/data/melb_data.csv', sep=',')

#print(melb_data.loc[15, 'Price'])
#print(melb_data.loc[90, 'Date'])
print(melb_data.columns)
#print(melb_data.loc[3521, 'Landsize']/melb_data.loc[1690, 'Landsize'])
melb_data['Postcode'] = melb_data['Postcode'].astype('int64')
melb_data['Car'] = melb_data['Car'].astype('int64')
melb_data['Bedroom'] = melb_data['Bedroom'].astype('int64')
melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
melb_data['Propertycount'] = melb_data['Propertycount'].astype('int64')
melb_data['YearBuilt'] = melb_data['YearBuilt'].astype('int64')
#melb_data.info()

#print(melb_data.describe().loc[:, ['Distance','BuildingArea', 'Price']])
#print(melb_data.describe(include=['object']))
#print(melb_data['Type'].value_counts(normalize=True))

#print(melb_data['Price'].mean())
#print(melb_data['Car'].max())

# rate = 0.12
# income = melb_data['Price'].sum()*rate
# print(f'Total income for agents: {round(income, 2)}')

# landsize_median = melb_data['Landsize'].median()
# landsize_mean = melb_data['Landsize'].mean()
# print(abs(landsize_median - landsize_mean)/landsize_mean)

#print(melb_data['Rooms'].mode())
#print(melb_data['Propertycount'].max())
# print(melb_data['Distance'].std())

# b_area_median = melb_data['BuildingArea'].median()
# b_area_mean = melb_data['BuildingArea'].mean()
# print((abs(b_area_median - b_area_mean)/b_area_mean)*100)

#print(melb_data['Bedroom'].value_counts(normalize=True))

# mask = melb_data['Price']>2000000
# print(melb_data[mask].head())

#print(melb_data[((melb_data['Rooms']==3)|(melb_data['BuildingArea']>100))&(melb_data['Price']<300000)].shape[0])
# print(melb_data[melb_data['Type']=='t']['Rooms'].max())

# mean_price = melb_data['Price'].mean()
# print(melb_data[melb_data['Price']>mean_price]['BuildingArea'].median())

# print(melb_data[melb_data['Bathroom']==0].shape[0])
# print(melb_data[(melb_data['SellerG']=='Nelson')&(melb_data['Price']>3000000)].shape[0])

# print(melb_data[melb_data['BuildingArea']==0]['Price'].min())

# print(melb_data[((melb_data['Rooms']>5)|(melb_data['YearBuilt']>2015))&(melb_data['Price']<1000000)]['Price'].mean())

print(melb_data[(melb_data['Type']=='h')&(melb_data['Price']<3000000)]['Regionname'].value_counts())