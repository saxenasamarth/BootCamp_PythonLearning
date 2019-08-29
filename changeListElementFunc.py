a =[1,2,3,7]
def func(v):
	v[0] =18

#print(a)
#func(a)
print(a)

def func2(v):
	#print(v)
	v =[3,5]
	print(v)

#print(a)
func2(a)
print(a) # this will print  global a, as the last function call could not modifyy global a