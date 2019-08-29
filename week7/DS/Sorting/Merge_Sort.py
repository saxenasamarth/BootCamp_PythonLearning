def merge(arr1, arr2):
	out = []
	i1, i2 = 0, 0
	for i in range(len(arr1)+len(arr2)):
		if i1 == len(arr1):
			return out + arr2[i2:]
		elif i2 == len(arr2):
			return out + arr1[i1:]
		elif arr1[i1]>arr2[i2]:
			out.append(arr2[i2])
			i2+=1
		else:
			out.append(arr1[i1])
			i1+=1
	
def merge_sort(arr):
	if len(arr)==1:
		return arr
	elif len(arr) == 2:
		return sorted(arr)
	else:
		mid = int(len(arr)/2)
		left = merge_sort(arr[:mid])
		right = merge_sort(arr[mid:])
		merged = merge(left, right)
		return merged
		
arr = [1, 6, 2, 8, 3, 10, 7]
out = merge_sort(arr)
print(out)		