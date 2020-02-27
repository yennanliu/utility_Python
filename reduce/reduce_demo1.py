"""
functools reduce op demo
"""
from functools import reduce


my_list = [1,2,3]

def accumulator(acc, item):
	print (acc, item)
	return acc + item


print ("my_list : ", my_list)
# reduce( function, dataset, initial_state)
print (reduce(accumulator, my_list, 0))
print ("-"*30)
print (reduce(accumulator, my_list, 10))
