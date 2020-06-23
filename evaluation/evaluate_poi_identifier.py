#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

total = len([e for e in labels_test if e == 1.0])

print('POIs in test set: ', total)
print('Predicted values length: ', len(pred))
print('Accuracy: ', accuracy_score(labels_test, pred))
print('Accuracy of biased identifier: ', float(1-(total/len(pred))))
print('Precision of biased identifier: ', precision_score(labels_test, pred))
print('Recall of biased identifier: ', recall_score(labels_test, pred))

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

true_positives = [i for (i,j) in zip(predictions, true_labels) if i == j]
print('True Positives in given Values: ', sum(true_positives))

true_negatives = len(true_positives) - sum(true_positives)
print('True Negatives in given Values: ', true_negatives)

false_positives = [i for (i,j) in zip(predictions, true_labels) if i != j]
print('False Positives in given values: ', sum(false_positives))

false_negatives = len(false_positives) - sum(false_positives)
print('False Negatives in given values: ', false_negatives)

print('Precision of given values: ', precision_score(true_labels, predictions))
print('Recall of given values: ', recall_score(true_labels, predictions))