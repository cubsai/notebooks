# %%
# Cell

from sklearn.datasets import load_iris
iris_dataset = load_iris()

# The iris object that is returned by load_iris is a Bunch object,
# which is very similar to a dictionary. It contains keys and values:

print("Keys of iris_dataset:\n", iris_dataset.keys())


# %%
# Cell 2

# The value of the key DESCR is a short description of the dataset.
# Feel free to look up the values of the other keys

print(iris_dataset['DESCR'][:193] + "\n...")


# %%
# Cell 3

# The value of the key target_names is an array of strings, containing
# the species of flower that we want to predict:

print("Target names:", iris_dataset['target_names'])


# %%
# Cell 4

# The value of feature_names is a list of strings, giving the 
# description of each feature:

print("Features names:\n", iris_dataset['feature_names'])


# %%
# Cell 5

# The data itself is contained in the target and data fields
# data contains the numeric measurements of sepal length, sepal width,
# petal length, and petal width in a NumPy array:

print("Type of data:", type(iris_dataset['data']))


# %%
# Cell 6

# The rows in the data array correspond to flowers, while the columns represent
# the four measurements that were taken for each flower:

print("Shape of data:", iris_dataset['data'].shape)

# %%
# Cell 7

# The array contains measurements for 150 different flowers.
# The individual items are called samples in maxchine learning, and their
# properties are called features.
# The shape of the data array is the number of samples times the number of features.
# This is the convention in sci-kit learn, and your data will always be assumed to be
# in this shape. Here are the feature values for the first ten samples:

print("First ten rows of data:\n", iris_dataset['data'][:10])

# %%
# Cell 8:

# The target array contains the species of each of the flowers that were measured, also as a NumPy array:

print("Type of target:", type(iris_dataset['target']))

# %%
# Cell 9:

# target is a one-dimensional array, with one entry per flower:

print("Shape of target:", iris_dataset['target'].shape)


# %%
# Cell 10:

# The species are encoded as integers from 0 to 2:

print("Target:\n", iris_dataset['target'])

# %%
# Cell 11:

# To assess the model's performance, we show it data that it did not see during training.
# This is usually done by splitting the labeled data collected into two parts - one part is 
# used to build the machine learning model, and is called the training data or training set.
# The rest of the data will be used to assess how well the model works; this is called the test
# data, test set, or hold-out set

# scikit-learn contains a function that shuffles the dataset and splits it for you: the train_test_split function

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)

# The output of the train_test_split function is X_train, X_test, y_train, and y_test, which are all NumPy arrays.
# X_train contains 75% of the rows of the dataset, and X_test contains the remaining 25%.

print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)

print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)

# %%
# Cell 12:

# Before building a machine learning model, it is often a good idea to inspect the data.
# to see if the task is easily solvable without machine learning, of if the desired information
# might not be contained in the data.

# One of the best ways to inspect data is to visualize it. One way to do this is by using a scatter plot.

# Let's do pair plots (of features). To create this plot, we first convert the NumPy array into a pandas DataFrame.
# pandas has a function to create pair plots called scatter_matrix

# create dataframe from data in X_train
# label the columns using the strings in iris_dataset.feature_names

import pandas as pd

iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)

# create a scatter matrix from the dataframe, colour by y_train

pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o', hist_kwds={'bins': 20}, s=60, 
alpha=.8)

# %%
# Cell 13:

# Building Your First Model: k-Nearest Neighbors
# The 'k' in k-nearest neigbors indicate that instead of using only the closest neighbor to classify a new data point,
# we can consider any fixed number of k neighbors in the training fit.

# All machine learning models in scikit-learn are implemented in their own classes, called Estimator classes.
# The k-nearest neighbors classification algorithm is implemeted in the KNeighborsClassifier class
# in the neighbors module.

# Before we can use the model, the class needs rto be instantiated into an object - this whenthe value of k is set

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

# The knn object encapsulates the algorithm that will be used to build the model frpm the training data,
# as well as the algorithm to make predictions on new data points. It will also hold the the information that
# the algorithm has extracted from the training data


# To build the model on the training set, we call the fit method of the knn object
# This takes as arguments the NumPy array X_train - the training data and the NumPy array y_train - corresponding training labels

knn.fit(X_train, y_train)


# %%
# Cell 14:

# Making predictions
# Using the model, predictions can now be made on new data not seen duiring training
# Imagine we've found an iris in the wild with the following features:
# Sepal length = 5 cm; Sepal width = 2.9 cm; Petal length = 1 cm; Petal width = 0.2 cm
# This new data needs to be put into a NumPy array

import numpy as np

X_new = np.array([[5, 2.9, 1, 0.2]])
print("X_new.shape", X_new.shape)



# %%
# Cell 15:

# To make a prediction, we call the predict method of the knn object:

prediction = knn.predict(X_new)
print("Prediction:", prediction)
print("Predicted target name:",iris_dataset['target_names'][prediction])


# %%
# Cell 16:

# Evaluating the model:

# The test set can now be used to evaluate the model
# Data in the Test set were not used to build the model
# We can, therefore, make a prediction for each iris in the test data set and compare it with its label
# We can then measure how well the model works by computing the accuracy in predicting the right species of flowers

y_pred = knn.predict(X_test)
print("Test set predictions:\n", y_pred)

# Computing the accuracy of the model:
print("\nTest set score: {:.2f}".format(np.mean(y_pred == y_test)))

# We can also use the score method of the knn object; this computes the accuracy of the model onthe test set for us
print("\nTest set score: {:.2f}".format(knn.score(X_test, y_test)))
