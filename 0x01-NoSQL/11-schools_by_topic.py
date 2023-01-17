#!/usr/bin/env python3
''' returns the list of school having a specific topic
'''


def schools_by_topic(mongo_collection, topic):
    query = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    value = mongo_collection.find(query)
    for v in value:
        return [v]
