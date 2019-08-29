class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.is_visited = False
		
	def get_sample():
		n1 = TreeNode(1)
		n2 = TreeNode(2)
		n3 = TreeNode(3)
		n4 = TreeNode(4)
		n5 = TreeNode(5)
		n6 = TreeNode(6)

		n4.left = n2
		n4.right = n5
		n2.right = n3
		n2.left = n1
		n5.right = n6
		return n4