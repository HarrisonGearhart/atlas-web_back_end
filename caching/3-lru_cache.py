#!/usr/bin/env python3
"""
LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Least Recently Used eviction policy caching system
    """

    def __init__(self):
        """
        Initialize LRUCache
        """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """
        Adds an item in the cache with a key using LRU replacement
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.access_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.access_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.access_order.append(key)

    def get(self, key):
        """
        Gets an item from cache from a key and mark as recently used
        """
        if key is not None and key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]

        return None
