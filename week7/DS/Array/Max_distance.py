#Maximum difference between two elements such that larger element appears after the smaller number

def max_difference(arr):
	min_found = arr[0]
	max_diff = 0
	for ele in arr[1:]:
		if ele < min_found:
			min_found = ele
		if ele-min_found > max_diff:
			max_diff = ele-min_found
	return max_diff

arr = [2, 4, 6, 10, 5, 1]
print(max_difference(arr))	