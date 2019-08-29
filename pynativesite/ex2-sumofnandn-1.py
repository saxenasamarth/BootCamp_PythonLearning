start = int(input("startNumber"))
stop=int(input("stopNumber"))
l=[]
v=0

for i in range(start,stop):
	l.append(i)
print(l)

for ind, val in enumerate(l):
	if ind==0:
		print(val+0)
		v = val
	else:
		print(val+v)
		v=val


