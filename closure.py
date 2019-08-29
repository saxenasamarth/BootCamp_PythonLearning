def func1():
	msg="hello world"
	def func2():
		print(msg)
	return func2

g =func1()
g()


#g=func1 call and establishes func2, does not execute it. and return func2, g()then corresponds to func(2) which executed print(msg)