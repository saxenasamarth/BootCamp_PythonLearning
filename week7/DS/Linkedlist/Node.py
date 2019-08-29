class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
		
	def get_sample():
		n1 = ListNode(1)
		n2 = ListNode(2)
		n3 = ListNode(3)
		n4 = ListNode(4)
		n5 = ListNode(5)
		n6 = ListNode(6)

		n1.next = n2
		n2.next = n3
		n3.next = n4
		n4.next = n5
		n5.next = n6
		return n1
		
def print_node_list(n1):
	curr = n1
	while(curr != None):
		print(curr.val, end =" ")
		curr = curr.next
	print()