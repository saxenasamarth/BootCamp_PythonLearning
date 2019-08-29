from Node import ListNode

def get_cycle_node(head):
	p1, p2 = head, head
	while(p1!=p2 or p1==head):
		p1 = p1.next
		p2 = p2.next.next
	p1 = head
	while(p1!=p2):
		p1 = p1.next
		p2 = p2.next
	return p1.val
	
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n8 = ListNode(8)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n5

print(get_cycle_node(n1))
	