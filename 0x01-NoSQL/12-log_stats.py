#!/usr/bin/env python3
'''Task 12 module
'''
from pymongo import MongoClient


def print_log(nginx_collection):
    total_count = nginx_collection.count_documents({})
    print('{} logs'.format(total_count))
    queries = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for query in queries:
        query_condition = {'method': query}
        method_count = nginx_collection.find({query_condition}).count()
        print('\tmethod {}: {}'.format(query, method_count))
    status = len(list(nginx_collection
                      .find({'method': 'GET', 'path': '/status'})))
    print('{} status check'.format(status))


def set_up():
    '''Print stats in a MongoDb Server
    '''
    cluster = MongoClient('mongodb://127.0.0.1:27017')
    print_log(cluster.logs.nginx)


if __name__ == '__main__':
    set_up()
