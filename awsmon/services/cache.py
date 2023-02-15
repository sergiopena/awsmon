from typing import Dict


class CacheService(object):
    def __init__(self, cache: Dict = {}):
        self.cache = cache

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value

    def delete(self, key):
        self.cache.delete(key)

    def flush(self):
        self.cache.flush_all()
