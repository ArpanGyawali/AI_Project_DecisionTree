from statistics import mean
import pandas as pd
import numpy as np
from decision_tree import DecisionTreeClassifier
from utils import *

def social_preprocess():
  #get the dataset
  col_names = ['User ID', 'Gender', 'Age', 'EstimatedSalary', 'Purchased']
  data = pd.read_csv("Social_Network_Ads.csv", skiprows=1, header=None, names=col_names)
  data['Gender'] = data['Gender'].astype('category')
  data['Gender'] = data['Gender'].cat.codes
  print(data.head(10))

  #train test split
  X = data.iloc[:, 1:-1].values   #ignoring User ID
  X, means, stdevs = standardize(X)             
  Y = data.iloc[:, -1].values.reshape(-1,1)
  # from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, Y, split=0.8)
  return X_train, X_test, y_train, y_test, means,stdevs
  
def covid_preprocess():
  #get the dataset
  data = pd.read_csv("covid_dataset.csv")
  print(data.head(10))

  #train test split
  X = data.iloc[:, 0:-1].values   #ignoring User ID       
  Y = data.iloc[:, -1].values.reshape(-1,1)
  # from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, Y, split=0.8)
  return X_train, X_test, y_train, y_test

def covid_get_model(X_train, y_train):
  #fit the model
  classifier = DecisionTreeClassifier(min_samples_split=18, max_depth=8)
  classifier.fit(X_train,y_train)
  classifier.print_tree()
  return classifier

def social_get_model(X_train, y_train):
  #fit the model
  classifier = DecisionTreeClassifier(min_samples_split=3, max_depth=5)
  classifier.fit(X_train,y_train)
  classifier.print_tree()
  return classifier

# if __name__=='__main__':
#   X_train, X_test, y_train, y_test = social_preprocess()
#   classifier = get_model(X_train, y_train)
#   #test the model
#   y_pred = classifier.predict(X_test) 
#   accuracy = accuracy_score(y_test, y_pred)
#   print("Accuracy: ", accuracy, "\n\n")
#   unique, matrix = confusion_matrix(y_test, y_pred)
#   print_confusion_matrix(unique, matrix)
#   # y_pred = classifier.predict(X_test) 
#   # from sklearn.metrics import accuracy_score
#   # print(accuracy_score(y_test, y_pred))

if __name__=='__main__':
  data = input('Enter the dataset(social or covid): ')
  if data == 'social':
    X_train, X_test, y_train, y_test, means, stdevs = social_preprocess()
    classifier = social_get_model(X_train, y_train)
    #test the model
    y_pred = classifier.predict(X_test) 
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: ", accuracy, "\n\n")
    unique, matrix = confusion_matrix(y_test, y_pred)
    print_confusion_matrix(unique, matrix)
  elif data == 'covid':
    X_train, X_test, y_train, y_test = covid_preprocess()
    classifier = covid_get_model(X_train, y_train)
    #test the model
    y_pred = classifier.predict(X_test) 
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: ", accuracy, "\n\n")
    unique, matrix = confusion_matrix(y_test, y_pred)
    print_confusion_matrix(unique, matrix)
  # y_pred = classifier.predict(X_test) 
  # from sklearn.metrics import accuracy_score
  # print(accuracy_score(y_test, y_pred))