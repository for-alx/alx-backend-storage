#!/usr/bin/env python3
"""
inserts a new document in a collection based on kwargs:
"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs:
        Args:
            mongo_collection (): pymongo collection object
            **kwargs ():
        Returns:
            Returns the new _id
    """
    id_object = mongo_collection.insert_one(kwargs)

    return id_object.inserted_id
