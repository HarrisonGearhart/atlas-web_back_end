#!/usr/bin/env python3
"""
Basic Cache class inherits from BaseCaching, is a caching system
"""
from base_cashing import BaseCaching

class BasicCache(BaseCaching):
    """
    defines BasicCache as a class that inherits from BaseCaching
    """
    def put(self, key, item):
        """
        adds item to cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        get an item from the cache by key
        """
        return (self.cache_data.get(key)) 
