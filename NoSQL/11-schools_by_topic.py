#!/usr/bin/env python3
"""
Gets a list of the schools that have a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    By topic
    """
    return list(mongo_collection.find({"topics": topic}))
