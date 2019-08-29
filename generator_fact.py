value =1
n=1

def gen_fun():
	global value
	global n
	while True:

		yield value
		n+=1
		value=value*n
		


b=gen_fun()
for i in range(6):
	print(next(b))
	

