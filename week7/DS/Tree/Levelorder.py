from Node import TreeNode

def levelorder_traversal(n):
	if n==None:
		return
	else:
		queue = [n]
		while(len(queue)!=0):
			node = queue.pop(0)
			print(node.val, end=" ")
			if node.left != None:
				queue.append(node.left)
			if node.right != None:
				queue.append(node.right)
				
n = TreeNode.get_sample()
levelorder_traversal(n)				