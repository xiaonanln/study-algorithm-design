import itertools

class AllSubsets(object):
	def __init__(self, N):
		self.N = N

	def run(self):
		print 'All subsets of N=%d:' % self.N
		inset = [False] * self.N
		def bt(i):
			if i == self.N:
				print [n for n, nin in enumerate(inset) if nin]
				return

			inset[i] = True
			bt(i+1)
			inset[i] = False
			bt(i+1)

		bt(0)

if __name__ == '__main__':
	AllSubsets(0).run()
	AllSubsets(1).run()
	AllSubsets(2).run()
	AllSubsets(3).run()
	AllSubsets(4).run()
	AllSubsets(5).run()

