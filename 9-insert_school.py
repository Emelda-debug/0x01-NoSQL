#!/usr/bin/env python3
"""
Python function that inserts a new document in a
collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Returns the new _id
    """
    new_id = mongo_collection.insert_one(kwargs)
    return new_id.inserted_id