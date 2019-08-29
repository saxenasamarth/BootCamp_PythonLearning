from Heap import HeapNode

def heapsort(array):
	h = HeapNode()
	h.heapify(array)
	while(len(h.heap) != 0):
		print(h.remove_min(), end=" ")
		
heapsort([7, 1, 9, 3, 6, 0])		
	