
class InsertionSort(object):
	def __init__(self, list):
		self.list = list

	def sort(self):
		for i in xrange(1, len(self.list)):
			# move i to proper position
			iv = self.list[i]
			ii = i
			while ii > 0 and iv < self.list[ii-1]:
				self.list[ii] = self.list[ii-1]
				ii -= 1

			self.list[ii] = iv

