import pandas as pd

nlo = pd.read_csv('~/pythonw/project1/data/nlo.csv', sep=',')

nlo['Time'] = pd.to_datetime(nlo['Time'])
nlo['Year'] = nlo['Time'].dt.year
nlo['Date'] = nlo['Time'].dt.date

int_days = nlo[nlo['State']=='NV']['Date'].diff().dt.days

print(int_days.mean())
