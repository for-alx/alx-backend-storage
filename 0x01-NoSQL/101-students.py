#!/usr/bin/env python3
"""
Returns all students sorted by average score:
"""
from collections import OrderedDict


def top_students(mongo_collection):
    """
        Args:
            mongo_collection (): pymongo collection object
        Returns:
            Returns all students sorted by average score:
    """
    pipe = [{'$addFields': {'averageScore': {'$avg': '$topics.score'}}},
            {'$sort': OrderedDict([('averageScore', -1), ('name', 1)])}]
    return mongo_collection.aggregate(pipe)
