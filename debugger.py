def debugger(func):
	def inner_function(*args, **kwargs):
		print("args {} kwargs {}".format([x for x in args],[(k,x) for k,x in kwargs.items()]))
		value=func(*args, **kwargs)
		return value
	return inner_function

@debugger
def fib(n):
	if n<=2:
		return 1
	else:
		return fib(n-1)+fib(n-2)



print(fib(5))
