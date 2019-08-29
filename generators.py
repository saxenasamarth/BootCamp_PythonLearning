import time
def do_nothing():
	time.sleep(1)

a = [do_nothing() for x in range(10)] # this forms list comprehension
b= (do_nothing() for x in range(10)) #round brackets makes this as generator and needs to be called, on need execution

print(a)
for val in b:
	print(val)
