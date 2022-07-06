import pandas as pd

orders = pd.read_csv('~/pythonw/project1/data/store/orders.csv',sep=';')
products = pd.read_csv('~/pythonw/project1/data/store/products.csv',sep=';')

print(orders.info())
print(products.info())

result = orders.merge(products, left_on='ID товара', right_on='Product_ID', how='left')
result['sum'] = result['Количество']*result['Price']
print(result.groupby('ID Покупателя')['sum'].sum())