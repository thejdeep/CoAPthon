from cachetools import LRUCache
from coapthon.caching.coapcache import CoapCache


class lifocache ():
    def __init__(self,max_dim=2048):
        self.stack=[]
        self.cachevalues={}
        self.maxsize=max_dim

    def update(self, elements):
        try:
            if (elements[0] not in self.cachevalues.keys()):
                if(len(self.cachevalues)==self.maxsize):
                    del self.cachevalues[self.stack[-1]]
                    del self.stack[-1]

                self.cachevalues[elements[0][0]]=elements[0][1]
                self.stack.append(elements[0][0])

            else: #Won't occur - only when element not in cache, it is brought
                self.cachevalues[elements[0][0]] = elements[0][1]
        except KeyError():
            self.cachevalues[elements[0][0]]=None

    def __getitem__(self, key):
        value = self.cachevalues[key]
        return value

    # def __setitem__(self, key, value):
    #     self.cachevalues[key]=value

    def currsize(self):
        return len(self.cachevalues)

    def items(self):
        "D.items() -> list of D's (key, value) pairs, as 2-tuples"
        return [(key, self.cachevalues[key]) for key in self.cachevalues.keys()]

    def keys(self):
        return [key for key in self.cachevalues.keys()]


class CoapLIFOCache(CoapCache):
    def __init__(self, max_dim):
        """

        :param max_dim:
        """
        print "Using LIFO Cache with dimension : " + str(max_dim)
        self.cache = lifocache(max_dim=max_dim)

    def update(self, key, element):
        """

        :param key:
        :param element:
        :return:
        """
        print "updating cache"
        print "key: ", key.hashkey
        print "element: ", element
        self.cache.update([(key.hashkey, element)])

    def get(self, key):
        """

        :param key:
        :return: CacheElement
        """
        try:
            print "Getting cache response"
            response = self.cache[key.hashkey]
        except KeyError:
            print "problem here"
            response = None
        return response

    def is_full(self):
        """
        :return:
        """
        if self.cache.currsize() == self.cache.maxsize:
            return True
        return False

    def is_empty(self):
        """

        :return:
        """

        if self.cache.currsize() == 0:
            return True
        return False

    def debug_print(self):
        """

        :return:
        """
        print "size = ", self.cache.currsize()
        list = self.cache.items()
        for key, element in list:
            print "element.max age ", element.max_age
            print "element.uri", element.uri
            print "element.freshness ", element.freshness

