from collections import defaultdict

class GraphNode:
	def __init__(self):
		self.neighbors = defaultdict(list)

	def add_neighbor(self, val1, val2):
		self.neighbors[val1].append(val2)
		self.neighbors[val2].append(val1)		
		
	def get_sample():
		n = GraphNode()
		n.add_neighbor(1, 5)
		n.add_neighbor(2, 3)
		n.add_neighbor(3, 6)
		n.add_neighbor(2, 8)
		n.add_neighbor(4, 8)
		n.add_neighbor(6, 7)
		n.add_neighbor(7, 1)
		return n		