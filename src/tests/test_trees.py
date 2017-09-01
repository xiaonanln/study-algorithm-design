from ch3 import BinaryTree

import unittest
import random
import sys

class TestTrees(unittest.TestCase):
	def testBinaryTree(self):
		self._testBinaryTree(BinaryTree.Insert, BinaryTree.Remove)

	def _testBinaryTree(self, insert, remove, repeat=100, treesize=1000):
		for _r in xrange(repeat):
			root = None
			vals = set()
			for _ts in xrange(treesize):

				n = random.randint(1, treesize * 10)
				root = insert(root, n)
				self.assertIsNotNone(BinaryTree.Search(root, n))
				vals.add(n)

			self.verifyGoodTree( root )
			BinaryTree.InOrder(root, lambda val: sys.stdout.write(str(val)+' '))
			sys.stdout.write('\n')
			BinaryTree.PreOrder(root, lambda val: val)
			BinaryTree.PostOrder(root, lambda val: val)
			BinaryTree.ByDepthOrder(root, lambda val: val)

			vals = list(vals)
			random.shuffle(vals)
			for n in vals:
				root = remove(root, n)
				self.assertIsNone(BinaryTree.Search(root, n))

			self.verifyGoodTree(root)

	def verifyGoodTree(self, root):

		def verifyHelper(root, minval, maxval):
			if root is None:
				return True

			if minval is not None and root.val <= minval:
				return False

			if maxval is not None and root.val >= maxval:
				return False

			return verifyHelper(root.left, minval, root.val) and verifyHelper(root.right, root.val, maxval)

		return verifyHelper(root, None, None)

if __name__ == '__main__':
	unittest.main()

