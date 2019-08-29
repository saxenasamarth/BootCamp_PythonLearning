from Node import ListNode, print_node_list

def get_nth_node_from_end(head, n):
	p1 = head
	p2 = head
	for i in range(n-1):
		p2 = p2.next
	while(p2.next != None):
		p1 = p1.next
		p2 = p2.next
	return p1.val

head = ListNode.get_sample()
print_node_list(head)
print(get_nth_node_from_end(head, 3))	