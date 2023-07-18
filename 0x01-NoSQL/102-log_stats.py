#!/usr/bin/env python3
"""
returns all students sorted by average score:
"""
from pymongo import MongoClient
from typing import Tuple
from collections import OrderedDict


def nginxStats():
    """
    comment
    """
    con: MongoClient = MongoClient()
    db = con.logs
    collection = db.nginx
    Methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    method_stats = []
    for met in Methods:
        method_count = collection.count_documents({'method': met})
        method_stats.append({'method': met, 'count': method_count})
    document_count = collection.estimated_document_count()
    status_path_stats = collection.count_documents({'method': 'GET',
                                                    'path': '/status'})
    pipeline = [{'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
                {'$sort': OrderedDict([('count', -1)])},
                {'$limit': 10}]
    top_ips = collection.aggregate(pipeline)
    con.close()
    return document_count, method_stats, status_path_stats, top_ips


def printStats():
    """
    comment
    """
    document_count, method_stats, status_path_stats, top_ips = nginxStats()
    print(f'{document_count} logs')
    print('Methods:')
    for method in method_stats:
        print(f'\tmethod {method.get("method")}: {method.get("count")}')
    print(f'{status_path_stats} status check')
    print('IPs:')
    for ip in top_ips:
        print(f'\t{ip.get("_id")}: {ip.get("count")}')


if __name__ == '__main__':
    printStats()
