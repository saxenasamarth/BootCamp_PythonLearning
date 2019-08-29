def checkinput(func):
	def inner_func(n):
		if n<1:
			raise ValueError
		else:
			value= func(n)
			return value
	return inner_func

@checkinput
def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)


n =int(input("pass the value"))
print(fact(n))