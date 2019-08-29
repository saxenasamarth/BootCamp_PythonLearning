from Node import ListNode, print_node_list

def reverse(head):
	curr = head
	prev = None
	while(curr != None):
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next
	return prev

head = ListNode.get_sample()
print("Original")		
print_node_list(head)
print("Reversed")		
head = reverse(head)
print_node_list(head)
	