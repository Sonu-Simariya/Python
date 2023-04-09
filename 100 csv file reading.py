import pandas as pd
file= pd.read_csv(r'C:/Users\deepajay\Downloads/Sample100.csv')
print(file[50:90])
print(file.head())
print(file.dtypes)
print(file.tail())
print(type(file['Serial Number']))
# 
print(file)
print(file[41:42])
print(file.loc[(file.Leave>4),('Employee Markme','Serial Number')])
print(file.iloc[50:60 ,3:5])
print(file.describe())
# from datetime import datetime as dt
# fl=dt.today()
# print(fl)
# hjflyujfuly
