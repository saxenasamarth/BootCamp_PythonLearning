# We are using a dequeu to store only important numbers. We always store the maximum number in current window at top. Whenever a new number is added if it is greater than existing max remove all numbers and keep only new number, else remove all numbers in dequeue from the back which are smaller than new number(we do this to keep only maximum numbers, if the new number is greater than few existing numbers in the window we dont need it). Also remove numbers from starting of dequeue if they are older than the current window.  

def sliding_window_maximum(nums, k):
	if(len(nums)<=1):
		return nums
	dq = [0]
	out = [0]
	for i in range(1, len(nums)):
		if nums[i] > nums[dq[0]]:
			dq = [i]
		else:
			while(len(dq)!=0):
				if nums[dq[-1]] < nums[i]:
					dq.pop()
				else:
					break
			dq.append(i)  
			while(len(dq)!=0):
				if dq[-1]-dq[0] >= k:
					dq.pop(0)
				else:
					break      
		out.append(dq[0])
	return [nums[i] for i in out][k-1:]
	
array = [1, 2, 3, 2, 4, 1, 5, 6, 1]
print(sliding_window_maximum(array, 3))	