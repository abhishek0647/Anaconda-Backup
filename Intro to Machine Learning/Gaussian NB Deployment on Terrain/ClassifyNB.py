# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 21:47:18 2016

@author: abhishek
"""

def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
        
    ### your code goes here!
    
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    return clf.fit(features_train, labels_train)
    