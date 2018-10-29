from __future__ import division
import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("F://python代码//kaggle数据//train.csv",)
label = df['TARGET']
df = df.drop(['ID','TARGET'],axis = 1)

##1.Basic Analysis##
#(1)Missing
missSet = [np.nan,9999999999,-999999]

len(df.iloc[:,0].unique())

count_un = df.iloc[:,0:3].apply(lambda x:len(x.unique()))

np.sum(df.iloc[:,0] == 0)

count_zero = df.iloc[:,0:3].apply(lambda x:np.sum(x == 0))

