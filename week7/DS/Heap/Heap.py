class HeapNode:
	def __init__(self):
		self.heap = []
		
	def percolate_up(self):
		i = len(self.heap)-1
		while(i>0):
			parent = self.heap[int((i-1)/2)]
			child = self.heap[i]
			if child < parent:
				self.heap[int((i-1)/2)], self.heap[i] = self.heap[i], self.heap[int((i-1)/2)]
				i = int((i-1)/2)
			else:
				break
	
	def insert(self, val):
		self.heap.append(val)
		if len(self.heap) != 0:
			self.percolate_up()
	

	def remove_min(self):
		if(len(self.heap) == 0):
			return
		val = self.heap[0]	
		self.heap[0] = self.heap[-1]
		self.heap.pop()
		i = 0
		while(i<int(len(self.heap)/2)):
			lindex = 2*i+1
			rindex = 2*i+2
			cindex = None
			if rindex == len(self.heap):
				cindex = lindex
			else:
				if self.heap[i] > self.heap[lindex] and self.heap[i] > self.heap[rindex]:
					if self.heap[lindex] > self.heap[rindex]:
						cindex = rindex
					else:
						cindex = lindex
				elif self.heap[i] > self.heap[lindex]:
					cindex = lindex
				elif self.heap[i] > self.heap[rindex]:
					cindex = rindex
				else:
					break
			self.heap[i], self.heap[cindex] = self.heap[cindex], self.heap[i]
			i = cindex
		return val	

	def heapify(self, array):
		for ele in array:
			self.insert(ele)
		
	@staticmethod	
	def get_sample():
		h = HeapNode()
		h.insert(5)
		h.insert(3)
		h.insert(8)
		h.insert(1)
		h.insert(6)
		h.insert(9)
		h.insert(2)
		return h
		
if __name__ == "__main__":	
	h = HeapNode.get_sample()
	print(h.heap)
	print(h.remove_min())
	print(h.heap)
	print(h.remove_min())
	print(h.heap)
	print(h.remove_min())
	print(h.heap)			