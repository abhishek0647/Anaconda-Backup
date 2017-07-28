# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 14:06:00 2016

@author: abhishek
"""

def classify(features_train, labels_train):    
    ### your code goes here--should return a trained decision tree classifer
    from sklearn import tree
    from sklearn.metrics import accuracy_score
    clf = tree.DecisionTreeClassifier()    
    clf = clf.fit(features_train, labels_train)

    return clf