# Give indices of two elements whose sum matches target 

def find_two_sum(arr, target):
	store_dict = {}
	for i, ele in enumerate(arr):
		if target-ele in store_dict:
			return store_dict[target-ele], i
		else:
			store_dict[ele] = i
			
arr = [2, 7, 11, 15]
print(find_two_sum(arr, 18))			