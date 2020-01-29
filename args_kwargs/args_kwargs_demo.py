def my_sample_func(*args, **kwargs):
	print ("*args : ", args)
	for i in args:
		print (i)
	print ("**kwargs : ", kwargs)
	k_dict = kwargs
	for j in k_dict.values():
		print (j)

if __name__ == '__main__':
	# 1,2,3 -> *args
	# num1=10, num2=11 -> **kwargs
	my_sample_func(1,2,3, num1=10, num2=11) 
	# -------------
	# python syntax rule :
	# params, *args, default parameters, **kwargs
	# e.g. f(name, 1,2,3, msg='hi', num1=10, num2=11)
	# -------------
