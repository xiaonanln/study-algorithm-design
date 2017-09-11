# coding: utf8
# 给一个整数集合s和一个整数n，请问s中是否存在一个子集合，这个集合里的元素和等于n

class SubsetSumProblem(object):
	def __init__(self, S, N):
		self.S = S
		self.N = N

	def run(self):
		S, N = self.S, self.N
		SS = len(S)
		use = [0] * N
		dp = [ [0] * (N+1) for _ in xrange(SS+1) ]
		for i in xrange(SS+1): dp[i][0] = 1

		for i in xrange(1, SS+1): # using subset S[:i], last elem is S[i-1]
			ln = S[i-1]
			for n in xrange(1, N+1): # sum `n` from 1 to N
				if n >= ln:
					dp[i][n] = dp[i-1][n] or dp[i-1][n-ln]
					if dp[i-1][n-ln]:
						use[i-1] = True
				else:
					dp[i][n] = dp[i-1][n]

		print '=' * 100
		print 'N=', self.N, 'Use=', use
		for _ in dp:
			print ''.join(map(lambda d: '%5d' % d, _))

		if dp[SS][N]:
			# get the sub set
			subset = []
			i, n = SS, N
			while i > 0 and n > 0:
				ln = S[i-1]
				if n >= ln and dp[i-1][n-ln]:
					subset.append(ln)
					i, n = i-1, n-ln
				else:
					assert dp[i-1][n]
					i, n = i-1, n

			print 'Subset:', subset, 'Sum:', sum(subset)


if __name__ == '__main__':
	SubsetSumProblem([], 0).run()
	SubsetSumProblem([1, 2, 3], 0).run()
	SubsetSumProblem([1, 2, 3], 1).run()
	SubsetSumProblem([1, 3, 4, 5, 6, 9], 18).run()
