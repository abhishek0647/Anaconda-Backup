# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 22:01:53 2016

@author: abhishek
"""

from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData
from classify import NBAccuracy

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()

def submitAccuracy():
    accuracy = NBAccuracy(features_train, labels_train, features_test, labels_test)
    print accuracy   
    return accuracy
    
submitAccuracy()