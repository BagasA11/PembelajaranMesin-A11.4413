import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import keras
# Importing the Keras libraries and packages
# from keras.models import Sequential
from keras import Sequential
from keras import Dense
# from keras.layers import Dense
from sklearn.metrics import confusion_matrix
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score


# Importing the dataset
dataset = pd.read_csv('./.xls/Churn_Modelling.csv')
# [baris, kolom]
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

print(X)
print(y)

labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
onehotencoder = ColumnTransformer([('one_hot_encoder', OneHotEncoder(),[1])], remainder = 'passthrough')
X = onehotencoder.fit_transform(X)
X = X[:, 1:]

print(X)

'''
[[0.0 0.0 619 ... 1 1 101348.88]
 [0.0 1.0 608 ... 0 1 112542.58]
 [0.0 0.0 502 ... 1 0 113931.57]
 ...
 [0.0 0.0 709 ... 0 1 42085.58]
 [1.0 0.0 772 ... 1 0 92888.52]
 [0.0 0.0 792 ... 1 0 38190.78]]
'''

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))

# Adding the second hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, epochs = 20)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred_ = (y_pred > 0.5)

# Making the Confusion Matrix

cm = confusion_matrix(y_test, y_pred_)

print(f"cm matriks: \n {cm}")

print(f"y_test: {y_test}")
print(f"y_pred_: {y_pred_}")
print(f"y_pred: {y_pred}")

# Menghitung confusion matrix
cm = confusion_matrix(y_test, y_pred_)
print("Confusion Matrix:\n", cm)

# Menghitung metrik performa
accuracy = accuracy_score(y_test, y_pred_)
precision = precision_score(y_test, y_pred_)
recall = recall_score(y_test, y_pred_)
f1 = f1_score(y_test, y_pred_)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)