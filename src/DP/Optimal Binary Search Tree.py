
# Given a sorted array keys[0.. n-1] of search keys and an array freq[0.. n-1] of frequency counts,
# where freq[i] is the number of searches to keys[i].
# Construct a binary search tree of all keys such that the total cost of all the searches is as small as possible.

class TreeNode(object):
	__slots__ = ('val', 'left', 'right')
	def __init__(self, val):
		self.val = val
		self.left = self.right = None

class OptimalBinarySearchTree(object):

	def __init__(self, vals, freq):
		assert len(vals) == len(freq)
		self.vals = vals
		self.freq = freq

	def run(self):
		vals, freq = self.vals, self.freq
		L = len(vals)

		dp = [ [0] * (L+1) for _ in xrange(L+1) ]
		rootdp = [ [-1] * (L+1) for _ in xrange(L+1) ]
		for l in xrange(1, L+1):  # l = 1 ~ L
			for i in xrange(0, L-l+1): # i = 0 ~ L-1
				j = i + l
				fsum = sum(vals[i:j])
				mindpval = float('inf')
				mindpindex = -1
				for k in xrange(i, j): # use each val as the root
					dpval = dp[i][k] + dp[k+1][j]
					if dpval < mindpval:
						mindpval = dpval
						mindpindex = k
				dp[i][j] = fsum + mindpval
				rootdp[i][j] = mindpindex

		print '=' * 100
		for _ in dp:
			print ''.join(map(lambda d: '%5d' % d, _))

		print '-' * 100
		for _ in rootdp:
			print ''.join(map(lambda d: '%5d' % d, _))

if __name__ == '__main__':
	OptimalBinarySearchTree([], []).run()
	OptimalBinarySearchTree([1, 2, 3], [1, 2, 3]).run()