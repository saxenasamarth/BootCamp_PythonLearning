from Node import TreeNode
from Inorder import inorder_traversal

def construct(inorder, postorder):
	if len(inorder) == 0 or len(postorder) == 0:
		return None
	else:
		root = postorder[-1]
		index = inorder.index(root)
		left_inorder = inorder[:index]
		right_inorder = inorder[index+1:]
		left_postorder = postorder[::-1][1+len(right_inorder):][::-1]
		right_postorder = postorder[::-1][1:1+len(right_inorder)][::-1] 
		root = TreeNode(root)
		root.left = construct(left_inorder, left_postorder)
		root.right = construct(right_inorder, right_postorder)
		return root
		
inorder = [1, 2, 3, 4, 5, 6]
postorder = [1, 3, 2, 6, 5, 4]
root = construct(inorder, postorder)
inorder_traversal(root)