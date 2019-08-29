def bubble_sort(arr):
	for i in range(len(arr)):
		index = i
		for j in range(i-1, -1, -1):
			if arr[j]>arr[index]:
				arr[j], arr[index] = arr[index], arr[j]
				index-=1
				
arr = [1, 6, 2, 8, 3, 10, 7]
bubble_sort(arr)
print(arr)				