# coding: utf8
# Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth (i.e., if you have a tree with depth D, you’ll have D linked lists).
# from collections import queue

from utils import *
from collections import deque

def getLevels(root):
	linkedLists = []
	if not root: return linkedLists

	q = deque()
	q.append(root)
	while q:
		qsize = len(q)
		head = tail = ListNode(None)
		for i in xrange(qsize):
			treenode = q.popleft()
			node = ListNode(treenode.val)
			tail.next = node
			tail = node

			if treenode.left: q.append(treenode.left)
			if treenode.right: q.append(treenode.right)

		linkedLists.append(head.next)

	return linkedLists




import utils

#   5
#  4  7
# 3   6 8
root = utils.maketree([1, 2, 2, None, 3, None, 3])
utils.printtree(root)
lists = getLevels(root)
for l in lists:
	utils.printlist(l )

