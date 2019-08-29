def partition(arr):
	pivot = arr[-1]
	i1 = 0
	for i2 in range(0, len(arr)-1):
		if arr[i2]<pivot:
			arr[i1], arr[i2] = arr[i2], arr[i1]
			i1+=1	
	return i1		

def quick_sort(arr):
	if len(arr) <= 1:
		return arr
	elif len(arr) == 2:
		return sorted(arr)
	else:
		index = partition(arr)
		left = quick_sort(arr[:index])
		right = quick_sort(arr[index:-1])
		return left+[arr[-1]]+right
		
arr = [1, 6, 2, 8, 3, 10, 7]
out = quick_sort(arr)
print(out)		