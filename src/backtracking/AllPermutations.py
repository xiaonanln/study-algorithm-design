import itertools

class AllPermutations(object):
	def __init__(self, N):
		self.N = N

	def run(self, m):
		print 'Calculating P(%d,%d): ' % (self.N, m)

		sol = [-1] * m
		used = [False] * self.N

		def bt(i):
			if i >= m:
				print tuple(sol)
				return

			for n, _used in enumerate(used):
				if not _used:
					used[n] = True
					sol[i] = n

					bt(i+1)

					used[n] = False

		bt(0)

if __name__ == '__main__':
	AllPermutations(4).run(0)
	AllPermutations(4).run(1)
	AllPermutations(4).run(2)
	AllPermutations(4).run(3)
	AllPermutations(4).run(4)
	AllPermutations(4).run(5)

