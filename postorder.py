from node import TreeNode

def postorder_traversal(n):
	if node ==None:
		return
	else:
		postorder_traversal(n.left)
		postorder_traversal(n.right)
		print(n.val, end=" ")

