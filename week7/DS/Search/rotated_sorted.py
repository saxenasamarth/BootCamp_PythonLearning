# Find pivot in rotated sorted array, search in a rotated sorted array

def find_rotated_sorted_pivot(arr):
	l, r = 0, len(arr)-1
	while(l <= r):
		mid = int((l+r)/2)
		if (mid==0 or arr[mid]<arr[mid-1]) and (mid==len(arr)-1 or arr[mid]<arr[mid+1]):
			return mid
		else:
			if arr[r] < arr[mid]:
				l = mid+1
			elif arr[r] > arr[mid]:
				r = mid-1
	return -1

arr = [6, 7, 8, 10, 12, 0, 2, 3, 4]
print(find_rotated_sorted_pivot(arr))
arr = [10, 12, 0, 2, 3, 4, 6, 7, 8]
print(find_rotated_sorted_pivot(arr))	