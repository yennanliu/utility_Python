#################################################################
# SCRIPT DEMO HOW TO CACHE ALREADY-COMPUTED VALUES   
#################################################################

# V1
# load cache module from python functools library 
#  http://book.pythontips.com/en/latest/function_caching.html?fbclid=IwAR3s_HdcP3pMBnDqYYW7dZ1K5Q4sSt5nhyb9Xdk7et7AsBpOYPbWz-uYhHU
from functools import lru_cache
@lru_cache(maxsize=32)
def add_one(x):
  print("compute y=x+1")
  y = x+1
  return y

# V2  
# UDF cache module
class Cacher:
  
  def __init__(self):
    self.computed = False
    self.data = None
  
  def save(self, data):
    print("save data to cache") # save cache to memory 
    self.data = data
    self.computed = True
  
  def read(self): 
    print("read data from cache") # read cache from memory 
    return self.data
  
  @property
  def is_computed(self):
    return self.computed # check if there is already computed cache data in memory 
  
  def clean_cache(self):
    self.data = None  # clean the cache in memory 
    self.computed = False
  
# cache decorator 
def cached(cacher: Cacher):
  def decorator(func):
    def cached_func(*arg, **kwarg):
      
      if cacher.is_computed: # if there is cache, get the data from cache 
        result = cacher.read()
        return result
      else: # if there is no data, compute then save to cache 
        result = func(*arg, **kwarg)
        cacher.save(result)
        return result    
      
    return  cached_func
  return decorator
 

# # create cache object instance 
# cacher = Cacher()
# # use the cache object instance  on add_one func 
# @cached(cacher)
# def add_one(x):
#   print("compute y=x+1")
#   y = x+1
#   return y

# input : 
# add_one(1)
# add_one(1)
# add_one(1)
# output : 
# compute y=x+1
# save data to cache
# read data from cache
# read data from cache
# 2
