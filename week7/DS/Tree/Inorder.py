from Node import TreeNode

def inorder_traversal(n):
	if n == None:
		return 
	else:
		inorder_traversal(n.left)
		print(n.val, end=" ")
		inorder_traversal(n.right)		

def inorder_traversal_iterative(n):
	stack = [n]
	while(len(stack) != 0):
		node = stack.pop()
		if node.is_visited:
			print(node.val, end=" ")
		else:	
			if node.right != None:
				stack.append(node.right)
			node.is_visited = True				
			stack.append(node)	
			if node.left != None:
				stack.append(node.left)		

if __name__ == '__main__':				
	n = TreeNode.get_sample()
	inorder_traversal(n)
	print()
	inorder_traversal_iterative(n)		