def Is_Symmetric(root1, root2):
	if root1 == None and root2 == None:
		return True
	elif root1 == None or root2 == None:
		return False
	else:
		return (root1.val == root2.val) and Is_Symmetric(root1.left, root2.right) and Is_Symmetric(root1.right, root2.left)
		
n1 = TreeNode(1)
n21 = TreeNode(2)
n22 = TreeNode(2)
n31 = TreeNode(3)
n41 = TreeNode(4)
n42 = TreeNode(4)
n32 = TreeNode(3)		

n1.left = n21
n1.right = n22
n21.left = n31
n21.right = n41
n22.left = n42
n22.right = n32

print(Is_Symmetric(n1))		