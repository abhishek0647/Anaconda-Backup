# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 14:03:15 2016

@author: abhishek
"""

#!/usr/bin/python

""" lecture and example code for decision tree unit """

import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from classifyDT import classify

features_train, labels_train, features_test, labels_test = makeTerrainData()


clf = classify(features_train, labels_train)

pred = clf.predict(features_test)

accuracy = accuracy_score(pred, labels_test)
prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())
print "Accuracy is ", accuracy
### the classify() function in classifyDT is where the magic
### happens--it's your job to fill this in!

#### grader code, do not modify below this line

