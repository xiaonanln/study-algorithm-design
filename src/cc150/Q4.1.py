# Implement a function to check if a tree is balanced.
# For the purposes of this question, a balanced tree is defined to be
# a tree such that no two leaf nodes differ in distance from the root by more than one.

import utils

def isBalanceTree(root):

	def isBalanceTreeHelper(root):
		if not root:
			return True, 0, 0

		lb, ls1, ls2 = isBalanceTreeHelper(root.left)
		rb, rs1, rs2 = isBalanceTreeHelper(root.right)
		if not lb or not rb:
			return False, -1, -1

		s1 = min(ls1, rs1)
		s2 = max(ls2, rs2)
		if s2 - s1 >= 2:
			return False, -1, -1

		return True, (1+s1), (1+s2)

	return isBalanceTreeHelper(root)[0]