import pandas as pd

studens_data = pd.read_csv('~/pythonw/project1/data/students_performance.csv', sep=',')
print(studens_data.columns)
#print(studens_data.shape)

#print(studens_data.loc[155, 'writing score'])

#print(studens_data.info())

#print(studens_data['math score'].mean())

#print(studens_data['race/ethnicity'].value_counts())

#print(studens_data[studens_data['test preparation course']=='completed']['reading score'].mean())

#print(studens_data[studens_data['math score']==0].shape[0])

#print(studens_data[studens_data['lunch']=='standard']['math score'].mean())
#print(studens_data[studens_data['lunch']=='free/reduced']['math score'].mean())

#mask = studens_data['parental level of education'] == "bachelor's degree"
#print(studens_data['parental level of education'].value_counts(normalize=True))

write_med_A = studens_data[studens_data['race/ethnicity']=="group A"]['writing score'].median();
write_med_c = studens_data[studens_data['race/ethnicity']=="group C"]['writing score'].median();
print(write_med_A - write_med_c)
