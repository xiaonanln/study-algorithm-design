
class LongestCommonSubsequence(object):
	def __init__(self, s1, s2):
		self.s1 = s1
		self.s2 = s2

	def run(self):
		s1, s2 = self.s1, self.s2
		dp = [ [0] * (len(s2)+1) for _ in xrange(len(s1)+1) ]
		for i in xrange(1, len(s1)+1):
			lc1  = s1[i-1]
			for j in xrange(1, len(s2)+1):
				lc2 = s2[j-1]

				ssl = max(dp[i-1][j], dp[i][j-1])
				if lc1 == lc2:
					ssl = max(ssl, dp[i-1][j-1]+1)

				dp[i][j] = ssl

		print '=' * 100
		for row in dp:
			print row

		# construct the substring from dp
		i, j = len(s1), len(s2)
		lcs = ''
		while i > 0 and j > 0:
			ssl = dp[i][j]
			if ssl == dp[i-1][j]:
				i, j = i-1, j
			elif ssl == dp[i][j-1]:
				i, j = i, j-1
			else:
				assert ssl == dp[i-1][j-1] + 1 and s1[i-1] == s2[j-1]
				lcs += s1[i-1]
				i, j = i-1, j-1

		lcs = lcs[::-1] # reverse the string

		print 'Length of LCS is %d, the string is %s' % (dp[len(s1)][len(s2)], lcs)


if __name__ == '__main__':
	LongestCommonSubsequence("", "").run()
	LongestCommonSubsequence("abc", "xabcd").run()
	LongestCommonSubsequence("xxxaaawefbefeffecwwwdeeeee", "aaaabbbbbccccccddddeeee").run()

