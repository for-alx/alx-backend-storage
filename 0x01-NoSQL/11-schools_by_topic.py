#!/usr/bin/env python3
"""
returns the list of school having a specific topic:
"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic:
        Args:
            mongo_collection (object): pymongo collection object
            topics (list): list of topics approached in the school
        Returns:
            returns the list of school
    """
    return mongo_collection.find({"topics": topic})
