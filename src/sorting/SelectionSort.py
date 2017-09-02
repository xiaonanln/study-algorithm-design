
class SelectionSort(object):
	def __init__(self, list):
		self.list = list

	def sort(self):
		N = len(self.list)
		for i in xrange(0, N):
			# find the minimal value from [i:] and put it to position i
			minpos, minval = i, self.list[i]
			for j in xrange(i+1, N):
				if self.list[j] < minval:
					minpos, minval = j, self.list[j]

			self.list[i], self.list[minpos] = self.list[minpos], self.list[i] # put minval to pos i
