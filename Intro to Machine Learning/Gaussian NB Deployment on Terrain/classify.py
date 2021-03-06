# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 22:02:20 2016

@author: abhishek
"""

def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score

    ### create classifier
    ### clf = #TODO
    clf = GaussianNB()
    clf.fit(features_train, labels_train)

    ### fit the classifier on the training features and labels
    #TODO

    ### use the trained classifier to predict labels for the test features
    ### pred = #TODO
    pred = clf.predict(features_test)

    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example, 
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    ### accuracy = #TODO
    accuracy = accuracy_score(pred, labels_test)
    return accuracy