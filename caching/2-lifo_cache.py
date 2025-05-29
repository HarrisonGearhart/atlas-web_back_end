#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    First-in/First-out caching system
    """

    def __init__(self):
        """
        Initialize LIFOCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Adds an item in the cache with a key using LIFO replacement
        """
        if key is None or item is None:
            return

        if (key not in self.cache_data
                and len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            newest_key = self.order.pop()
            del self.cache_data[newest_key]
            print(f"DISCARD: {newest_key}")

        if key not in self.order:
            self.order.append(key)

        self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from cache from a key
        """
        if key is not None:
            return self.cache_data.get(key, None)

        return None
