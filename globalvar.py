a = 5
b= 7
def sumof(a,b):
	a =19 # it will create a new variable a inside the fun and use it
	return a+b

#print(sumof(a,b))
#print(a) # this will still print global a which is unaltered

a = 20
def incrementof():
	a=0 # need to initialise a variable if it has same name as a global variable
	a = a + 1 # this will throw error(if above line i.e. local initialisation of variable is not done), because a =a +1 means you are assigning a new value to awhich is not initialisedinside the function.
	print(a)

def decrementof():
	global a
	a-=1
	print(a)


incrementof()
decrementof()

