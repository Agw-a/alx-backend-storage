#!/usr/bin/env python3
'''Task 8 module
'''


def list_all(mongo_collection):
    """returns list of all documents

    Args:
        mongo_collection:pymongo collection object
    Returns:
        list: all documents
    """
    my_doc = mongo_collection.find()
    for i in my_doc:
        return [i]
