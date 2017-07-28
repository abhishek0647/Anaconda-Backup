# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 23:01:12 2016

@author: abhishek
"""

import simpleTFIDF

table = simpleTFIDF.tfidf()
table.addDocument("foo", ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel"])
table.addDocument("bar", ["alpha", "bravo", "charlie", "india", "juliet", "kilo"])
table.addDocument("baz", ["kilo", "lima", "mike", "november"])

print table.similarities (["alpha", "bravo", "charlie"]) # => [['foo', 0.6875], ['bar', 0.75], ['baz', 0.0]]