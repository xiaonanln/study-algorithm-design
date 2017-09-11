
class Knapsack01(object):
	def __init__(self, T, items):
		self.T = T
		self.items = items

	def run(self):
		T, items = self.T, self.items
		self.dp = dp = [[0] * (len(items) + 1) for _ in xrange(T + 1)]
		print '=' * 80
		print 'Put items %s to T=%d' % (items, T)

		for t in xrange(1, T+1):
			for n in xrange(1, len(items)+1):
				lw, lv = items[n-1]
				r = dp[t][n-1]
				if t >= lw:
					r = max(r, lv + dp[t-lw][n-1])
				dp[t][n] = r

		for row in dp:
			print row

		print 'Maxinum value: %d' % dp[T][len(items)]

	def getPackedItems(self):
		t, n = self.T, len(self.items)
		items = []
		while t > 0 and n > 0:
			lw, lv = self.items[n-1]
			t_, n_ = t, n-1

			if self.dp[t][n] > self.dp[t_][n_]:
				assert t >= lw
				items.append(self.items[n-1])
				t_, n_ = t-lw, n-1

			t, n = t_, n_

		return list(reversed(items))


if __name__ == '__main__':
	def runKnapsack01(T, items):
		alg = Knapsack01(T, items)
		alg.run()
		print 'Packed items:', alg.getPackedItems()

	runKnapsack01(0, [])
	runKnapsack01(0, [(1, 2), (2, 3)])
	runKnapsack01(10, [(1, 2), (2, 3), (3, 4), (4, 13), (5, 6), (6, 7), (8, 9), (9, 20)])
