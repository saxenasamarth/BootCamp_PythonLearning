from Node import TreeNode
import sys
def isValidBST(root, max_val, min_val):
	if root == None:
		return True
	else:
		if root.val > max_val or root.val < min_val:
			return False
		else:
			if (root.left!=None and root.val < root.left.val) or (root.right!=None and root.val > root.right.val):
				return False
			else:
				return isValidBST(root.left, root.val, min_val) and isValidBST(root.right, max_val, root.val)
				
head = TreeNode.get_sample()
print(isValidBST(head, sys.maxsize, -sys.maxsize-1))				


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)

n4.left = n2
n4.right = n5
n2.right = n3
n2.left = n1
n5.right = n6
n3.right = n7
print(isValidBST(n4, sys.maxsize, -sys.maxsize-1))		