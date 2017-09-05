
import time
import unittest
from unionfind.MyStupidUnionFind import  MyStupidUnionFind
from unionfind.UnionFind import UnionFind

class TestUnionFind(unittest.TestCase):

	def testMyStupidUnionFindTiny(self):
		self._testUnionFind(MyStupidUnionFind, 'tiny', 10000)

	def testMyStupidUnionFindMedium(self):
		self._testUnionFind(MyStupidUnionFind, 'medium', 100)

	# def testMyStupidUnionFindLarge(self):
	# 	self._testUnionFind(MyStupidUnionFind, 'large', 1)

	def testUnionFindTiny(self):
		self._testUnionFind(lambda N: UnionFind(N), 'tiny', 10000)

	def testUnionFindMedium(self):
		self._testUnionFind(lambda N: UnionFind(N), 'medium', 100)

	def testUnionFindLarge(self):
		self._testUnionFind(lambda N: UnionFind(N), 'large', 1)

	def _testUnionFind(self, unionFindCreater, datasize, repeat):
		fd = open('data/%sUF.txt' % datasize, 'rt')

		pairs = []
		with fd:
			N = int(fd.readline().strip())

			for line in fd:
				x, y = line.strip().split()
				x, y = int(x), int(y)
				pairs.append((x, y))

		print 'read %sUF.txt ok' %datasize
		t0 = time.time()
		for _ in xrange(repeat):
			uf = unionFindCreater(N)
			if datasize == 'large': print 'UF created'
			for i, (x, y) in enumerate(pairs):
				uf.union(x, y)
				assert uf.find(x) == uf.find(y)
				if (i+1) % 10000 == 0:
					print (i+1), '/', len(pairs)

		dt = time.time() - t0
		print 'UnionFind %s on %s data takes %.1f ms' %(unionFindCreater, datasize, dt*1000)