#!/usr/bin/env python3
"""
class FIFOCache inherits from BaseCaching, is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Class to FIFO data
    """
    # inherit from parent BaseCaching
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        adds an item to the cache
        """
        # if there is a key and an item
        # value of key is the value of item
        if key and item:
            self.cache_data[key] = item
            # if number of items in cache_data is more than max_items
            # then we del the first
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # iterate through keys, and break right at first key
                for keys in self.cache_data:
                    first = keys
                    break
                print("DISCARD:", first)
                # then delete the first key we just located
                del self.cache_data[first]

    def get(self, key):
        """
        get an item from the cache by key
        """
        # when using get method, if key is not there then it returns none
        return (self.cache_data.get(key))
