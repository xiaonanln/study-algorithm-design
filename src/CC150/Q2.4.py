# coding: utf8
# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1’s digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
#
# EXAMPLE
#
# Input: (3 -> 1 -> 5), (5 -> 9 -> 2)
#
# Output: 8 -> 0 -> 8

import utils

def sum(h1, h2):
	head = tail = None
	p1, p2 = h1, h2
	C = 0
	while p1 or p2 or C:
		val = (p1.val if p1 else 0) + (p2.val if p2 else 0) + C
		if val >= 10:
			val = val % 10
			C = 1
		else:
			C = 0

		node = utils.ListNode(val)

		if head is not None:
			tail.next = node
			tail = node
		else:
			head = tail = node

		if p1: p1 = p1.next
		if p2: p2 = p2.next

	return head



h1 = utils.makelist(3, 1, 5)
h2 = utils.makelist(5, 9, 2)
utils.printlist(h1)
utils.printlist(h2)
utils.printlist(sum(h1, h2))


h1 = utils.makelist(1)
h2 = utils.makelist(9, 9, 9)
utils.printlist(h1)
utils.printlist(h2)
utils.printlist(sum(h1, h2))

