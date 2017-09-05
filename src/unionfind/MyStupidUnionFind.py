
# this is the stupid union-find soluion I gave for

class MyStupidUnionFind(object):

	def __init__(self, N):
		self.sets = [set([n]) for n in xrange(N)]

	def find(self, x):
		return self.sets[x]

	def union(self, x, y):
		sx = self.sets[x]
		sy = self.sets[y]
		if sx is sy:
			return

		if len(sx) < len(sy):
			sx, sy = sy, sx

		# let sx merge sy
		sx |= sy
		for n in sy:
			self.sets[n] = sx
