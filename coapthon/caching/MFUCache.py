from coapthon.caching.coapcache import CoapCache
from cachetools import Cache
import collections

class MFUCache(Cache):
    """Most Frequently Used (MFU) cache implementation."""

    def __init__(self, maxsize, missing=None, getsizeof=None):
        Cache.__init__(self, maxsize, missing, getsizeof)
        self.__counter = collections.Counter()

    def __getitem__(self, key, cache_getitem=Cache.__getitem__):
        value = cache_getitem(self, key)
        self.__counter[key] += 1
        return value

    def __setitem__(self, key, value, cache_setitem=Cache.__setitem__):
        cache_setitem(self, key, value)
        self.__counter[key] += 1

    def __delitem__(self, key, cache_delitem=Cache.__delitem__):
        cache_delitem(self, key)
        del self.__counter[key]

    def popitem(self):
        """Remove and return the `(key, value)` pair least frequently used."""
        try:
            (key, _), = self.__counter.most_common(1)
        except ValueError:
            raise KeyError('%s is empty' % self.__class__.__name__)
        else:
            return (key, self.pop(key))