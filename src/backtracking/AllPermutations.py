import itertools

class AllPermutations(object):
	def __init__(self, N):
		self.N = N

	def run(self, m):
		print 'Calculating P(%d,%d): ' % (self.N, m)
		for x in itertools.per

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
	AllPermutations(4).run(0)
	AllPermutations(4).run(1)
	AllPermutations(4).run(2)
	AllPermutations(4).run(3)
	AllPermutations(4).run(4)
	AllPermutations(4).run(5)

