# Product of array except self

def product_except_self(arr):
	out = [1]
	for i in range(1, len(arr)):
		out.append(out[-1]*arr[i-1])
	right = 1	
	for i in range(len(arr)-1, -1, -1):
		out[i] = out[i]*right	
		right = right * arr[i]
	return out

arr = [1, 2, 3, 4]
print(product_except_self(arr))	