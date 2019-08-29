from Node import TreeNode
from Inorder import inorder_traversal
def sorted_array_to_bst(array):
	if len(array) == 0:
		return None
	elif len(array) == 1:
		return TreeNode(array[0])
	else:
		mid = int(len(array)/2)
		root = TreeNode(array[mid])
		root.left = sorted_array_to_bst(array[:mid])
		root.right = sorted_array_to_bst(array[mid+1:])
		return root
		
array = [1, 2, 3, 4, 5, 6]
root = sorted_array_to_bst(array)
inorder_traversal(root)		