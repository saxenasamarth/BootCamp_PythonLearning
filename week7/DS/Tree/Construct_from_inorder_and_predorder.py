from Node import TreeNode
from Inorder import inorder_traversal

def construct(inorder, preorder):
	if len(inorder) == 0 or len(preorder) == 0:
		return None
	else:
		root = preorder[0]
		index = inorder.index(root)
		left_inorder = inorder[:index]
		right_inorder = inorder[index+1:]
		left_preorder = preorder[1:1+len(left_inorder)]
		right_preorder = preorder[1+len(left_inorder):]
		root = TreeNode(root)
		root.left = construct(left_inorder, left_preorder)
		root.right = construct(right_inorder, right_preorder)
		return root
		
inorder = [1, 2, 3, 4, 5, 6]
preorder = [4, 2, 1, 3, 5, 6]
root = construct(inorder, preorder)
inorder_traversal(root)		