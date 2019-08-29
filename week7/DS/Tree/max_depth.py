from Node import TreeNode

def max_depth(root):
	if root == None:
		return 0
	else:
		return 1 + max(max_depth(root.left), max_depth(root.right))
		
root = TreeNode.get_sample()
print(max_depth(root))		