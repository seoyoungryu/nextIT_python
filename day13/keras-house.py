import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split

df = pd.read_csv("../data/house_train.csv")
result = df.isnull().sum().sort_values(ascending=False).head(20)
print(result)

#one-hot encoding
df = pd.get_dummies(df)

# 데이터가 없는 부분을 채워줌
df = df.fillna(df.mean())

df_corr = df.corr()
df_corr_sort = df_corr.sort_values('SalePrice', ascending=False)
print(df_corr_sort['SalePrice'].head(10))
cols = ['SalePrice','OverallQual','GrLivArea','GarageCars','GarageArea','TotalBsmtSF']
sns.pairplot(df[cols])
plt.savefig('house-corr')

cols_train = ['OverallQual','GrLivArea','GarageCars','GarageArea','TotalBsmtSF']
X = df[cols_train]

y = df['SalePrice'].values

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

#model
model = Sequential()
model.add(Dense(10, input_dim=X_test.shape[1], activation='relu'))
model.add(Dense(30, activation='relu'))
model.add(Dense(40, activation='relu'))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')

