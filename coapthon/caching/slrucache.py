from coapthon.caching.coapcache import CoapCache


class slrucache():
    def __init__(self,max_dim=2048):
        print "Using SLRU Cache with dimension : " + str(max_dim)
        self.stack_probationary = []
        self.stack_protected = []
        self.cachevalues={}
        self.maxsize=max_dim

    def update(self, elements):
        try:
            if (elements[0] not in self.cachevalues.keys()):
                if(len(self.stack_probationary)==self.maxsize):
                    del self.cachevalues[self.stack_probationary[-1]]
                    self.stack_probationary.pop()

                self.cachevalues[elements[0][0]]=elements[0][1]
                self.stack_probationary.insert(0,elements[0][0])

            else:
                self.cachevalues[elements[0][0]] = elements[0][1]
                try:
                    x = self.stack_probationary.index(elements[0][0])
                    del self.stack_probationary[x]
                except ValueError:
                    x = self.stack_protected.index(elements[0][0])
                    del self.stack_protected[x]
                if(len(self.stack_protected)==self.maxsize):
                    temp = self.stack_protected.pop()
                    if(len(self.stack_probationary)==self.maxsize):
                        flag = self.stack_probationary.pop()
                        del self.cachevalues[flag]
                    self.stack_probationary.insert(0,temp)
                self.stack_protected.insert(0,elements[0][0])


        except KeyError():
            self.cachevalues[elements[0][0]]=None

    def __getitem__(self, key):
        value = self.cachevalues[key]
        return value

    def currsize(self):
        return len(self.cachevalues)

    def items(self):
        return [(key, self.cachevalues[key]) for key in self.cachevalues.keys()]

    def keys(self):
        return [key for key in self.cachevalues.keys()]


class CoapSLRUCache(CoapCache):
    def __init__(self, max_dim):
        """

        :param max_dim:
        """
        self.cache = slrucache(max_dim=max_dim)

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

