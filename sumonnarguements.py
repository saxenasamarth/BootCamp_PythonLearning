n =input("give n values")
b =n.split(",")
l =[]
for x in b:
	z=int(x)
	l.append(z)


def sumof(argv):
	sum=0
	for i in argv:

		sum=sum+i
	return sum


print(sumof(l))





'''def sumofall(*args):
	total =0
	for num in args:
		total=total +num
	return total


print(sumofall(1,3,4,5))
'''

