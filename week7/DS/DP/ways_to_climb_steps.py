def climb_steps_ways(n):
	a = 1 # For 1 step
	b = 2 # For 2 steps
	for i in range(3, n+1):
		b, a = a+b, b
	return b
	
print(climb_steps_ways(5))	