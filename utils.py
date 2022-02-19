from random import randrange
import numpy as np
import math

def accuracy_score(actual, predicted):
  correct = 0
  for i in range(len(actual)):
    if actual[i] == predicted[i]:
      correct += 1
  return correct / float(len(actual)) * 100.0

def confusion_matrix(actual, predicted):
  actual = np.squeeze(actual, 1)
  unique = set(actual)
  matrix = [list() for x in range(len(unique))]
  for i in range(len(unique)):
    matrix[i] = [0 for x in range(len(unique))]
  lookup = dict()
  for i, value in enumerate(unique):
    lookup[value] = i
  for i in range(len(actual)):
    x = lookup[actual[i]]
    y = lookup[predicted[i]]
    matrix[y][x] += 1
  return unique, matrix

# def label_encoder(label):
#   unique_label = set(label)
#   catagory = [i for i in len(unique_label)]
#   encoded_label = list()
#   for label in encoded_label:
#     for i in range(unique_label):
#       label = 



def print_confusion_matrix(unique, matrix):
  print('(A)' + ' '.join(str(x) for x in unique))
  print('(P)---')
  for i, x in enumerate(unique):
    print("%s| %s" % (x, ' '.join(str(x) for x in matrix[i])))

def train_test_split(datasetX, datasety, split=0.60):
  trainX = list()
  trainy = list()
  train_size = split * len(datasetX)
  datasetX_copy = list(datasetX)
  datasety_copy = list(datasety)
  while len(trainX) < train_size:
    index = randrange(len(datasetX_copy))
    trainX.append(datasetX_copy.pop(index))
    trainy.append(datasety_copy.pop(index))
  return trainX, datasetX_copy, trainy, datasety_copy


# calculate column means
def column_means(dataset):
	means = [0 for i in range(len(dataset[0]))]
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		means[i] = sum(col_values) / float(len(dataset))
	return means
 
# calculate column standard deviations
def column_stdevs(dataset, means):
	stdevs = [0 for i in range(len(dataset[0]))]
	for i in range(len(dataset[0])):
		variance = [pow(row[i]-means[i], 2) for row in dataset]
		stdevs[i] = sum(variance)
	stdevs = [math.sqrt(x/(float(len(dataset)-1))) for x in stdevs]
	return stdevs
 
# standardize dataset
def standardize(dataset):
  dataset = dataset.astype('float32')
  means = column_means(dataset)
  stdevs = column_stdevs(dataset, means)
  for row in dataset:
    for i in range(len(row)):
      row[i] = (row[i] - means[i]) / stdevs[i]
  return dataset, means, stdevs
  

