# coding: utf8
"""
Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.

DEFINITION

Circular linked list: A (corrupt) linked list in which a node’s next pointer points to an earlier node, so as to make a loop in the linked list.

EXAMPLE

Input: A -> B -> C -> D -> E -> C [the same C as earlier]

Output: C
"""

import utils
head = utils.makelist(*"ABCDE")
utils.printlist(head)
head[4].next = head[2]
# utils.printlist(head)

def containsLoop(head):
	if head is None: return False
	sp = fp = head
	while True:
		if fp.next is None or fp.next.next is None:
			return False

		sp = sp.next
		fp = fp.next.next
		if sp == fp:
			return True

def getLoopStartNode(head):
	if head is None: return None
	sp = fp = head
	while True:
		if fp.next is None or fp.next.next is None:
			return None

		sp = sp.next
		fp = fp.next.next
		if sp == fp:
			break

	p = head
	while p is not sp:
		p = p.next
		sp = sp.next

	return p



print containsLoop(head)
print getLoopStartNode(head )