from Node import GraphNode

def DFS_helper(node, vertex, visited):
	print(vertex, end=" ")
	visited[vertex] = True
	for neighbor in node.neighbors[vertex]:
		if neighbor not in visited:
			DFS_helper(node, neighbor, visited)
			
def DFS_run(node):
	visited = {}
	for vertex in node.neighbors:
		if vertex not in visited:
			DFS_helper(node, vertex, visited)

n = GraphNode.get_sample()
DFS_run(n)