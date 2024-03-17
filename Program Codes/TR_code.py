import pandas as pd

df = pd.read_csv('dataset.csv')

df

df.isnull().sum()

df.dtypes

x = df.iloc[:, :13]
y = df.iloc[:, 13:14]

x

y

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

y_train

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(x_train.values, y_train)

knn.predict(x_test)

y_test

knn.score(x_test, y_test)*100
df.columns

import pickle
with open("TR_Model.pkl", "wb") as f:
  pickle.dump(knn, f)

import pickle
with open("TR_Model.pkl", "rb") as f:
  model=pickle.load(f)

print(f)

