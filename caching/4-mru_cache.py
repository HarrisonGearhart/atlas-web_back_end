#!/usr/bin/env python3
"""
class MRUCache inherits from BaseCaching/is a caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Class to LIFO data
    """
    # inherit from parent BaseCaching
    def __init__(self):
        super().__init__()
        # list to hold used data
        self.used = []

    def put(self, key, item):
        """
        adds an item to the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.used.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # most recently used
            mru = self.used.pop()
            # Discard mru
            print("DISCARD:", mru)
            # then delete the last key we just located
            del self.cache_data[mru]

        # add the new key
        self.cache_data[key] = item
        # and update used list
        self.used.append(key)

    def get(self, key):
        """
        get an item from the cache by key
        """
        # when using get method, if key is not there then it returns none
        # if the key exists remove it
        if key not in self.cache_data:
            return None
        if key in self.used:
            self.used.remove(key)
        # append list with new key
        self.used.append(key)
        return (self.cache_data.get(key))
        