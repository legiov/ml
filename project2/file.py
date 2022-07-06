import pandas as pd
import os


df = pd.read_csv('project2/data/countries.csv')
df.to_csv('project2/data/countries.txt', index=False, sep='&')
df.merge(suffixes=('_bronze', '_silver'))
