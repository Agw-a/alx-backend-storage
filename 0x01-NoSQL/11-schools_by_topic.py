#!/usr/bin/env python3
''' returns the list of school having a specific topic
'''


def schools_by_topic(mongo_collection, topic):
    """returns list of schools with topics

    Args:
        mongo_collection: pymongo coll. object
        topic (str): topic to search

    Returns:
        list with result
    """
    query_condition = {'topics': {'$eq': topic}}
    return [result for result in mongo_collection.find(query_condition)]
