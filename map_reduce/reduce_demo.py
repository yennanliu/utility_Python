#################################################################
# PYTHON REDUCE EXAMPLE 
#################################################################

# https://thepythonguru.com/python-builtin-functions/reduce/
from functools import reduce
def do_sum(x1, x2): return x1 + x2

def do_mul(x1, x2): return x1*x2 


if __name__ == '__main__':
	print (reduce(do_sum, [1,2,3,4]))
	print (reduce(do_mul, [1,2,3,4]))
