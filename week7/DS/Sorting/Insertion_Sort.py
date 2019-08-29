def insertion_sort(arr):
	for i in range(1, len(arr)):
		val = arr[i]
		index = i
		for j in range(i-1, -1, -1):
			if arr[j] > val:
				index-=1
		arr.pop(i)		
		arr.insert(index, val)

arr = [1, 6, 2, 8, 3, 10, 7]
insertion_sort(arr)
print(arr)		