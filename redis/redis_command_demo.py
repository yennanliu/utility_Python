# python3 
# https://redis.io/topics/quickstart
# https://github.com/andymccurdy/redis-py
# http://www.runoob.com/redis/redis-strings.html

from redis import StrictRedis
from redis import ConnectionPool

# ------------------------------------------------------
# CONFIG 
# CONNECT TO redis METHOD 1) 
redis = StrictRedis(host='localhost', port=6397, db=0)
# CONNECT TO redis METHOD 2) 
pool = ConnectionPool(host='localhost', port=6397, db=0)
redis = StrictRedis(ConnectionPool)
# CONNECT TO redis METHOD 3)  : via URL
# redis = StrictRedis.from_url(url='redis://localhost:6379/1')
# CONNECT TO redis METHOD 4)  : via URL
pool = ConnectionPool.from_url('redis://@localhost:6379/1')
redis = StrictRedis(connection_pool=pool)
# ------------------------------------------------------

# OP demo 
# 1)  simple set key-value and query 
import redis
r = redis.Redis(host='127.0.0.1', port=6379)
r.set('key1', 'abc')
print (r.get('key1'))   

# ------------------------------------------------------
# 2) multiple  set key-value   : PIPELINE

pipe = r.pipeline(transaction=True)   
r.set('name', 'Lisi')                   
r.set('role', 'male')
pipe.execute()                     
print (r.get('name'))
print (r.get('role'))

# ------------------------------------------------------
# 3) more PIPELINE

r.set('bing', 'baz')
# Use the pipeline() method to create a pipeline instance
pipe = r.pipeline()
# The following SET commands are buffered
pipe.set('foo', 'bar')
pipe.get('bing')
pipe.get('foo')
# the EXECUTE call sends all buffered commands to the server, returning
# a list of responses, one for each command.
pipe.execute()
