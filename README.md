# REDIS-pickle
A slightly modified version of the StrictRedis class in redis-py, providing convenience methods for caching and retrieving complex Python objects.

This (very small) module provides a object class based on redis-py's "StrictRedis" class, with two convenience methods ("pset" and "pget") that automatically pickle and unpickle objects placed in the memcache.  This pickling enables complex Python objects, such as DataFrames, to be cached.  It would be possible to add pickle versions of all other StrictRedis (or Redis) methods that store or retrieve data--I don't have any personal use for these at the moment, and therefore haven't added them myself, but I invite anyone who'd like to to fork this repo.

Note that pickling may be unsafe if a pickled object includes executable code.  An alternative method is to convert objects to JSON strings, but this will be unwieldy in many cases--and it isn't necessary for data that doesn't come from external sources outside your control.  See this Stack Overflow question for details:

http://stackoverflow.com/questions/15219858/how-to-store-a-complex-object-in-redis-using-redis-py
