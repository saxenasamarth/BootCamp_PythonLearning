from Node import TreeNode

class BST:
	def insert(self, root, value):
		if root == None:
			return
		else:
			if root.val > value:
				if root.left == None:
					root.left = TreeNode(value)
				else:
					self.insert(root.left, value)
			else:
				if root.right == None:
					root.right = TreeNode(value)
				else:
					self.insert(root.right, value)
					
	def search(self, root, value):
		if root == None:
			return root
		else:
			if root.val == value:
				return root
			elif root.val > value:
				return self.search(root.left, value)
			else:
				return self.search(root.right, value)
	
	def find_closest(self, root):
		if root.right == None:
			return root.val
		else:
			return self.find_closest(root.right)
				
	def delete(self, root, value):
		if root == None:
			return
		else:
			if root.val == value:
				if root.left == None and root.right == None:
					return None
				elif root.left == None:
					return root.right
				elif root.right == None:
					return root.left
				else:
					closest = self.find_closest(root.left)
					root.val = closest
					self.delete(root.left, closest)
					return root
			elif root.val > value:
				root.left = self.delete(root.left, value)
			else:
				root.right = self.delete(root.right, value)
				
	def inorder_traversal(self, root):
		if root == None:
			return 
		else:
			self.inorder_traversal(root.left)
			print(root.val, end=" ")
			self.inorder_traversal(root.right)

b = BST()
root = TreeNode.get_sample()
b.inorder_traversal(root)
print()
b.insert(root, 9)
b.inorder_traversal(root)
print()
print(b.search(root, 3))
print(b.search(root, 7))
b.delete(root, 4)
b.inorder_traversal(root)			