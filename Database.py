#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:24:34 2024

@author: ramintork
"""
import pymongo

class Database(object):
    URI = "mongodb+srv://hackuser:Saturday1Sfun@cluster0.wq5qa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    DATABASE = None
    
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['sample_airbnb']
        
    def find_one(collection,query):
        return Database.DATABASE[collection].find_one(query)
    
