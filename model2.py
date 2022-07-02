# Import necessary modules
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import numpy as np
import csv
import pandas as pd
import pickle

dfrm = pd.read_csv(
    'c:/Users/User/Desktop/burty/Angular/fyp/src/app/datasetPanicAtt.csv')

# Create feature and target arrays
X = dfrm.drop(['level'], axis=1)
y = dfrm['level']

# Split the dataset training and test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(X_train, y_train)

standardize = preprocessing.StandardScaler()

pickle.dump(knn, open("model.pkl", "wb"))

def prototype(data_to_predict):
    data_to_predict = data_to_predict
    data_to_predict_df = pd.DataFrame(data_to_predict)
    data_to_predict_df
    data_to_predict_std = standardize.fit_transform(data_to_predict_df)
    predictions = knn.predict(data_to_predict_std)
    str1 = ""
    for i in predictions:
      str1 += i
    return str1
