from collections import deque
class UnionFind(object):

	def __init__(self, N):
		self.sets = range(N)
		self.rank = [0] * N

	def find(self, x):
		s = self.sets[x]
		if s == x:
			return s

		ss = self.find(s)
		if ss != s: self.sets[x] = ss # path compression
		return ss

	def union(self, x, y):
		sx = self.find(x)
		sy = self.find(y)
		self.sets[sy] = sx
		# union by rank, but actually slows down UF in test
		# rx, ry = self.rank[sx], self.rank[sy]
		# if rx > ry:
		# 	self.sets[sx] = sy
		# elif rx < ry:
		# 	self.sets[sy] = sx
		# else:
		# 	self.sets[sy] = sx
		# 	self.rank[sx] = rx + 1

	def connected(self, x, y):
		return self.find(x) == self.find(y)
