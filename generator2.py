'''Write a generator which gives the time user takes to call the function from previous call
(Time between current next() call and previous next() call). 
Store a local variable to reference previous time, calculate current time at every next call on generator and yield their difference. 
Update previous time before return for next call'''
import time
prevtime = time.time()

def timecalc():
	global prevtime
	print("printing")
	while(True):
		currenttime=time.time()
		x=prevtime
		prevtime=currenttime
		yield currenttime-x
		


b=timecalc()

print(next(b))
time.sleep(5)
print(next(b))
	





