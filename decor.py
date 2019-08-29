import time


def rate_limiter(func):
	def inner_func(*args, **kwargs):
		print("sleeping for 1 secs")
		time.sleep(1)
		value=func(*args, **kwargs)
		return value
	return inner_func


@rate_limiter
def takeinp():
	fname=input("enter first name")



takeinp()
