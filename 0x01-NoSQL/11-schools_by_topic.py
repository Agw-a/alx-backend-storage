#!/usr/bin/env python3
''' returns the list of school having a specific topic
'''


def schools_by_topic(mongo_collection, topic):
    query_condition = {'topics': {'$eq': topic}}
    return [result for result in mongo_collection.find(query_condition)]
