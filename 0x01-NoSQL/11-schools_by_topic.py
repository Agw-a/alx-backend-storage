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
    return [val for val in mongo_collection.find(query)]
