#!/usr/bin/env python3
"""
Change school topics
"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name:
        Args:
            mongo_collection (object): pymongo collection object
            name (str):  school name to update
            topics (list): list of topics approached in the school
        Returns:
            none
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
