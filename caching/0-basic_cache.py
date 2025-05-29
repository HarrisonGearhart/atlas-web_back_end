#!/usr/bin/env python3
"""
BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Caching system that doesn't limit items
    """

    def put(self, key, item):
        """
        Adds an item in the cache with a key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from the cache from a key
        """
        if key is not None:
            return self.cache_data.get(key, None)

        return None
