

class MatrixChainMultiplication(object):
	def __init__(self, *seq):
		self.seq = seq
		self.assureSeqValid(seq)

	def run(self):
		if not self.seq:
			return 0

		seq, seqlen = self.seq, len(self.seq)
		dp = self.dp = [[0] * (seqlen+1) for _ in xrange(seqlen+1)]
		for ssl in xrange(1, seqlen+1): # for all subsequence of length l
			for i in xrange(0, seqlen - ssl + 1): # subsequence seq[i:i+l)
				j = i + ssl # subsequence seq[i:j)
				dp[i][j] = max([dp[i][k] + dp[k][j] + seq[k - 1][1] * seq[k][0] for k in xrange(i+1, j)] or [0]) # 2 subsequence: seq[i:k) and seq[k:j)

		print '=' * 100
		for _ in dp:
			print ''.join(map(lambda d: '%5d' % d, _))

		print 'Final cost is %d' % (dp[0][seqlen])

		# dp = self.dp = [[0] * (seqlen) for _ in xrange(seqlen)]
		# for ssl in xrange(1, seqlen+1): # for all subsequence of length l
		# 	for i in xrange(0, seqlen - ssl + 1): # subsequence seq[i:i+l)
		# 		j = i + ssl - 1 # subsequence seq[i:j]
		# 		dp[i][j] = max([dp[i][k] + dp[k+1][j] + seq[k][1] * seq[k+1][0] for k in xrange(i, j)] or [0]) # 2 subsequence: seq[i:k] and seq[k+1:j]
		#
		# print '=' * 100
		# for _ in dp:
		# 	print ''.join(map(lambda d: '%5d' % d, _))
		#
		# print 'Final cost is %d' % (dp[0][seqlen-1])

	def assureSeqValid(self, seq):
		if not seq:
			return True

		m = seq[0][1]
		for i in xrange(1, len(seq)):
			a, b = seq[i]
			assert m == a
			m = b

if __name__ == '__main__':
	MatrixChainMultiplication().run()
	MatrixChainMultiplication((1, 2), (2, 3), (3, 4), (4, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1)).run()





