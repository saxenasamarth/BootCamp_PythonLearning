from Heap import HeapNode
def kth_smallest_number(array, k):
	h = HeapNode()
	h.heapify(array)
	for i in range(k-1):
		h.remove_min()
	return h.remove_min()

array =  [7, 1, 9, 3, 6, 0]
print(kth_smallest_number(array, 4))	