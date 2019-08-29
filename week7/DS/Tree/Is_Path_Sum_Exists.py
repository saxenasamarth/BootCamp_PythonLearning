from Node import TreeNode

def is_path_sum_exists(root, val):
	if root == None:
		return val == 0
	else:
		return is_path_sum_exists(root.left, val-root.val) or is_path_sum_exists(root.right, val-root.val)
		
n = TreeNode.get_sample()
print(is_path_sum_exists(n, 9))		
print(is_path_sum_exists(n, 16))		