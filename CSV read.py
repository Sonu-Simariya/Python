import pandas as pt

file=pt.read_csv(r'C:/Users\deepajay\Downloads/10000 Sales Records.csv')
print(file)
print(file['Region'])
print(file.describe())
print(file.loc[(file.Total_Profit>=411291.95),('Total_Profit','Country','Region','Ship Date')])
Drop the column
y=file.drop(columns='Country')
Add Column
y=file['trigger']='yes'
print(y)
print(file.head(50))
