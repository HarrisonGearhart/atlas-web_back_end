#!/usr/bin/env python3
"""
Lists all docs in a MongoDB collection
"""

def list_all(mongo_collection):
    """
    Return an empty list if no document in the collection
    """
    return list(mongo_collection.find())
