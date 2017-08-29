from ch3 import BinaryTree

import unittest
import random
import sys
from ch4 import Heap

class TestHeap(unittest.TestCase):
	def testHeap(self):
		for i in xrange(100):
			heap = [random.randint(1, 1000) for _ in xrange(random.randint(100, 1000))]
			Heap.Heapify( heap )
			heapsize = len(heap)
			sorting = []
			while heap:
				sorting.append(Heap.Pop(heap))

			self.assertEqual(heapsize, len(sorting))
			self.checkSorted(sorting)

	def checkSorted(self, list):
		lastVal = None
		for v in list:
			if lastVal is not None:
				assert v >= lastVal

			lastVal = v


if __name__ == '__main__':
	unittest.main()

