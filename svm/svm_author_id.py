#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

from sklearn import svm
from sklearn.metrics import accuracy_score

clf = svm.SVC(kernel='rbf', C=10000)

# Slicing to 1% of the dataset for low training time but reduced accuracy
#features_train = features_train[:int(len(features_train)//100)]
#labels_train = labels_train[:int(len(labels_train)//100)]

t0 = time()
clf.fit(features_train, labels_train)
print("Training time:", round(time()-t0, 3), "s")

t1 = time()
pred = clf.predict(features_test) # Zero-indexed list
print("Prediction time:", round(time()-t1, 3), "s")

print('Score: ', accuracy_score(labels_test, pred))

def check_Chris(pred):
    n = 0

    for p in pred:
        if p == 1:
            n+=1

    return n

print('Chris prediction no.: ', check_Chris(pred))