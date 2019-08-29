def max_subarray(array):
	if len(array) == 0:
		return 0
	else:
		curr_so_far = array[0]
		max_so_far = curr_so_far
		for i in range(1, len(array)):
			if curr_so_far < 0 and array[i] >= 0:
				curr_so_far = array[i]
				max_so_far = max(max_so_far, curr_so_far)
			else:
				curr_so_far = curr_so_far + array[i]
				max_so_far = max(max_so_far, curr_so_far)
		return max_so_far
		
array = [-2,1,-3,4,-1,2,1,-5,4]		
print(max_subarray(array))		