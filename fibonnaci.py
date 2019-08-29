def fib(n):
	if n==1:
		return 1
	elif n==2:
		return 1
	else:
		result= fib(n-1) + fib(n-2)
		print(result)
	return result

print(fib(4))