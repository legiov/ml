import pandas as pd
from pandas.tseries.offsets import Hour, Second
df = pd.read_csv('~/pythonw/project1/data/citibike-tripdata.csv', sep=',')



#print(df['bikeid'].value_counts())

rows_count = df.shape[0]

sub_count = df[df['usertype']== 'Subscriber'].shape[0]
cus_count = df[df['usertype']== 'Customer'].shape[0]
#print(sub_count/rows_count)

men = df[df['gender']==1].shape[0]
women = df[df['gender']==2].shape[0]
#print(df['start station id'].nunique())
#print(df['end station id'].nunique())

df['starttime'] = pd.to_datetime(df['starttime'])
df['stoptime'] = pd.to_datetime(df['stoptime'])
age = df['birth year'].apply(lambda x: 2018 - x)
#print(age.min())
#print(df['end station name'].value_counts())
df = df.drop(['start station id', 'end station id'], axis=1)
df['age'] = age
df = df.drop('birth year', axis=1)


#print(df[df['age']>60].shape[0])

df['trip duration'] = df['stoptime'] - df['starttime']
df['trip duration'] = df['trip duration'].dt.seconds


#print(df['trip duration'].mean())
df['weekend'] = df['starttime'].apply(lambda x: 1 if x.dayofweek > 4 else 0)


print(df[df['weekend']==1].shape[0])

def time_of_day(date):
    if date.hour < 7:
        return 'night'
    elif date.hour < 13:
        return 'morning'
    elif date.hour < 19:
        return 'day'
    else:
        return 'evening'
    
df['time of day'] = df['starttime'].apply(time_of_day) 

print(df.info())
print(df.head(5)) 

night = df[df['time of day']=='night'].shape[0]
day = df[df['time of day']== 'day'].shape[0]
print(day/night)