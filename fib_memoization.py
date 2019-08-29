memo={}

memo ={1:1,2:1}

def fib(n):
	
	
	if n==1:
		return memo[1]
	if n==2:
		return memo[2]
	if n-1 in memo:
		v1  = memo[n-1]

	else:
		v1=fib(n-1)
		memo[n-1]=v1
	if n-2 in memo:
		v2 = memo[n-2]
	else:
		v2=fib(n-2)
		memo[n-2]=v2
	return v1+v2


print(fib(12))
print(memo)