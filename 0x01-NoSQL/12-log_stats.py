#!/usr/bin/env python3
"""
Log stats
"""


from pymongo import MongoClient


if __name__ == '__main__':
    """Log stats"""
    connection = MongoClient('mongodb://localhost:27017')
    collection = connection.logs.nginx

    print(f'{collection.estimated_document_count()} logs')

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')

    for request in methods:
        print('\tmethods {}: {}'.format(request,
              collection.count_documents({'method': request})))

    print('{} status check'.format(collection.count_documents(
          {'method': 'GET', 'path': '/status'})))
