import random
import time
import timeit
import unittest

from ch2.InsertionSort import InsertionSort
from ch2.SelectionSort import SelectionSort
from ch4.HeapSort import HeapSort
from ch4.MergeSort import MergeSort
from ch4.QuickSort import QuickSort
from ch4.QuickSortW3 import QuickSortW3
from ch4.ShellSort import ShellSort
from ch4.RadixSortLSD import RadixSortLSD

class TestSort(unittest.TestCase):
	def testInsertionSort(self):
		self._testSort(InsertionSort)

	def testSelectionSort(self):
		self._testSort(SelectionSort)

	def testHeapSort(self):
		self._testSort(HeapSort)

	def testMergeSort(self):
		self._testSort(MergeSort)

	def testQuickSort(self):
		self._testSort(QuickSort)

	def testQuickSortW3(self):
		self._testSort(QuickSortW3)

	def testShellSort(self):
		self._testSort(ShellSort)

	def testRadixSortLSD(self):
		self._testSort(RadixSortLSD)


	def genRandomList(self, length):
		return [ random.randint(1, length//50) for _ in xrange(length)]

	def _testSort(self, sorterClass):
		print '====================================================================================================='
		for length in (1000, 2000, 4000, 8000, 10000, 100000):
			if length >= 5000 and sorterClass in (InsertionSort, SelectionSort, ShellSort):
				continue

			list = self.genRandomList(length)
			t0 = time.time()
			sorterClass(list).sort()
			dt = time.time() - t0
			self.checkSorted(list)
			print '%s sort on %d nums => %.3fms' % (sorterClass.__name__, length, dt * 1000)

	def checkSorted(self, list):
		lastVal = None
		for v in list:
			if lastVal is not None:
				assert v >= lastVal, '%s and %s is not in order' % (lastVal, v)

			lastVal = v


if __name__ == '__main__':
	unittest.main()
