from Node import TreeNode

def postorder_traversal(n):
	if n == None:
		return 
	else:
		postorder_traversal(n.left)
		postorder_traversal(n.right)	
		print(n.val, end=" ")		
		
def postorder_traversal_iterative(n):
	stack = [n]
	while(len(stack) != 0):
		node = stack.pop()
		if node.is_visited:
			print(node.val, end=" ")
		else:	
			node.is_visited = True				
			stack.append(node)			
			if node.right != None:
				stack.append(node.right)
			if node.left != None:
				stack.append(node.left)								
		
n = TreeNode.get_sample()
postorder_traversal(n)
print()
postorder_traversal_iterative(n)