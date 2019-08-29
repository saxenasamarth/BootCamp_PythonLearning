from Node import TreeNode

def preorder_traversal(n):
	if n == None:
		return 
	else:
		print(n.val, end=" ")
		preorder_traversal(n.left)
		preorder_traversal(n.right)		
		
def preorder_traversal_iterative(n):
	stack = [n]
	while(len(stack) != 0):
		node = stack.pop()
		if node.is_visited:
			print(node.val, end=" ")
		else:	
			if node.right != None:
				stack.append(node.right)
			if node.left != None:
				stack.append(node.left)				
			node.is_visited = True				
			stack.append(node)			
		
n = TreeNode.get_sample()
preorder_traversal(n)
print()
preorder_traversal_iterative(n)