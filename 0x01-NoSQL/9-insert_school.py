#!/usr/bin/env python3
'''Task 9 module
'''


def insert_school(mongo_collection, **kwargs):
    '''inserts a new document into a collection
    '''
    posts = mongo_collection.insert_one(kwargs)
    return posts.inserted_id
