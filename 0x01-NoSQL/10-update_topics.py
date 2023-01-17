#!/usr/bin/env python3
'''Changes all topuics of a document
'''


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document

    Args:
        mongo_collection : pymongo collection object
        name (string): will be the school name to update
        topics (List[str]): the list of topics approached in the school
    """
    query = {'name': name}
    new_values = {'$set': {'topics': topics}}
    mongo_collection.update_many(query, new_values)
