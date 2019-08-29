from Node import GraphNode

def BFS_run(node):
	visited = {}
	queue = []
	for vertex in node.neighbors:
		if vertex not in visited:
			queue.append(vertex)
			while(len(queue) != 0):
				n = queue.pop(0)
				#print("Popped", n, queue)
				if n not in visited:
					visited[n] = True
					print(n, end=" ")
					#print("Neighbors", node.neighbors[n])
					for neighbor in node.neighbors[n]:
						queue.append(neighbor)
						
n = GraphNode.get_sample()
BFS_run(n)						