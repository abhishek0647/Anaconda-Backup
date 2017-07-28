# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 01:20:58 2017

@author: abhishek
"""

from elasticsearch import Elasticsearch
import json
import timeit

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#start = timeit.default_timer()
#with open('/Users/abhishek/Downloads/datasets/movie_metadata.json') as json_file:
#  json_data = json.load(json_file)
#stop = timeit.default_timer()
#print "Time taken to load json: " + str(stop-start) + " seconds"

#start = timeit.default_timer()
#i=1
#while i<=len(json_data):
#  es.index(index='imdb', doc_type='movies', id=i, body=json_data[i-1])
#  i+=1  
#stop = timeit.default_timer()
#print "Time taken to create the index: " + str(stop-start) + " seconds"

#print es.get(index='imdb', doc_type='movies', id=5)
#print es.search(index="imdb", body={"query": {"match": {'director_name':'Doug'}}})

start = timeit.default_timer()
#print es.search(index="imdb", body={"query": {"prefix": {'movie_title':'Avengers'}}})
print es.search(index="imdb", body={"query": {"multi_match": {"fields": ["movie_title"], "query": "Avtar", "fuzziness": "AUTO"}}})
stop = timeit.default_timer()
print "Time taken to search the json: " + str(stop-start) + " seconds"
