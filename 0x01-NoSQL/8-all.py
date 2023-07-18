#!/usr/bin/env python3
"""
lists all documents in a collection:
"""


def list_all(mongo_collection):
    """ lists all documents in a collection:
        Args:
            mongo_collection (): pymongo collection object
        Returns:
            lists all documents in a collection:
    """
    found = mongo_collection.find()

    return [doc for doc in found]
