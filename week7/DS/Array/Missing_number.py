# Find missing number from group of n numbers

def missing_number(arr):
	return (((len(arr)+2)*(len(arr)+1))/2)-sum(arr)
	
arr = [1, 2, 3, 5, 6, 7]
print(missing_number(arr))
arr = [1, 2, 3, 4, 5, 7, 8]
print(missing_number(arr))	