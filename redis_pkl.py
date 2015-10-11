from redis import StrictRedis
import cPickle as pickle

# This sub-class of the StrictRedis class incorporates pickling and unpickling
# through "pset" and "pget" methods that replace the "set" and "get" methods,
# thereby enabling the caching of complex object classes.

class PickledRedis(StrictRedis):

    def pset(self, key, value, ex=None, px=None, nx=False, xx=False):
        value_pickled = pickle.dumps(value, 2)
        return self.set(key, value_pickled, ex=None, px=None, nx=False, xx=False)    
        
    def pget(self, key):
        value_pickled = self.get(key)
        return pickle.loads(value_pickled)
