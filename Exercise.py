from statistics import correlation
import array as arr
import numpy as np
import LinearRegression as LR
import matplotlib.pyplot as mlp
import pandas as pd
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from collections import Counter
import chart_studio.plotly as cs 
from plotly.offline import init_notebook_mode, plot, iplot
import plotly.graph_objs as go

# house_price_datasets = sklearn.datasets.load_boston()
# print(house_price_datasets.DESCR)
# house_df=pd.DataFrame(house_price_datasets.data, columns=house_price_datasets.feature_names)
# print(house_df.head())
# print(house_df.__len__())
# print(house_df.shape)
# house_df['price']=house_price_datasets.target
# print(house_df)
# print(house_price_datasets.keys())
# print(house_df.describe())
# 
# correlation= house_df.corr()
# x=mlp.figure(figsize=(10,10))
# y=sns.heatmap(correlation, cbar=True, square=True, fmt=".1f", annot_kws=('size',8), cmap="spring")
# 
# print(x,y)
# 
data= pd.read_csv(r'C:/Users\deepajay\Downloads/Sheet.csv')
print(data)
print(data.keys())
d=data.loc[(data.Approx_Hour>=1),('Day','Subject','Approx_Hour')]
print(d.tail())
print(data.iloc[4:60])

# mlp.plot(data.loc[(data.Subject=='Physics'),'Subject'])
# mlp.plot(data.loc[(data.Day=='Monday'),'Subject'])
# mlp.xlabel('subject')
# mlp.ylabel('Approx_Hours')
# mlp.show()


Subject=Counter(data.Subject)
Approx_Houb=Subject.most_common()
print(Approx_Houb)

x, y=zip(Approx_Hour)
x, y= list(x), list(y)
Subject=pd.DataFrame(x)
day=pd.DataFrame(y)
date=pd.concat([Subject.iloc[:, 0],day.iloc[:, 0]],axis=1)
date.columns= "Subject","Approx_Hours"
data.head(10)


# mlp.plot(np.sin(90))
# mlp.xlabel('x label')
# mlp.ylabel('y label')
# mlp.show()
