from Node import TreeNode

def postorder_traversal(n):
	if n ==None:
		return
	else:
		postorder_traversal(n.left)
		postorder_traversal(n.right)
		print(n.val, end=" ")



if __name__=='__main__':
	n=TreeNode.get_sample()
	postorder_traversal(n)
	print()
