def func(a, b=50):
	print(a,b)


func(5)
func(5,60)

def func2(a,b=30,c=40):
	print(a,b,c)

func2(3,c=5)

# unknown number of arguements
def func(*argv):
	for arg in argv:
		print(arg)


print(func(1,2,5,7))


#keyword arguements

def func(*argv, **kwargs):
	
	for key, arg in kwargs.items():
		print(key, arg)

	for key in kwargs:
		print(key)

	for arg in argv:
		print(arg)

print(func(7,8,45, a=5, b=12,c=54))

# return n number of args

def func3(a,b):
	return a*b, a+b
print(func3(7,8))

c,d = func3(7,8)
print(c)
print(d)


square = lambda x:x*x
print(square(5))

incr = lambda x:x+1
print(incr(7))


#using function as a variable

def func4(a,b):
	return a+b

g =func4
print(g(1,7))




#pass function as an arguement

def func5(functionname , variable1 ,variable2):
	return functionname(variable1, variable2)

print(func5(func4, 2,7))


# returning function from function
def func6():
	return func4

print(func6()(1,5))
#above func6() returns func4 and utilises 1,5 as func4(1,5)