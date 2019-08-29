def binary_search(arr, target):
	out = -1
	l, r = 0, len(arr)-1
	while(l<=r):
		mid = int((l+r)/2)
		if arr[mid] == target:
			out = mid
			break
		elif arr[mid] > target:
			r = mid-1
		else:
			l = mid+1
	return out

arr = [1, 3, 6, 7, 12, 24, 34, 45, 56]

print(binary_search(arr, 6))
print(binary_search(arr, 45))
print(binary_search(arr, 1))
print(binary_search(arr, 56))
print(binary_search(arr, 100))	

def binary_search_find_rightmost(arr, target):
	out = -1
	l, r = 0, len(arr)-1
	while(l<=r):
		mid = int((l+r)/2)
		if arr[mid]==target:
			out = mid
			l = mid+1
		elif arr[mid]>target:
			r = mid-1
		else:
			l = mid+1
	return out		
	
arr = [1, 3, 3, 7, 7, 7, 12, 12, 23, 23, 23, 34, 34, 34, 34, 56]

print(binary_search_find_rightmost(arr, 3))
print(binary_search_find_rightmost(arr, 23))
print(binary_search_find_rightmost(arr, 1))
print(binary_search_find_rightmost(arr, 56))
print(binary_search_find_rightmost(arr, 100))

def binary_search_find_leftmost(arr, target):
	out = -1
	l, r = 0, len(arr)-1
	while(l<=r):
		mid = int((l+r)/2)
		if arr[mid]==target:
			out = mid
			r = mid-1
		elif arr[mid]>target:
			r = mid-1
		else:
			l = mid+1
	return out		
	
print(binary_search_find_leftmost(arr, 3))
print(binary_search_find_leftmost(arr, 23))
print(binary_search_find_leftmost(arr, 1))
print(binary_search_find_leftmost(arr, 56))
print(binary_search_find_leftmost(arr, 100))		