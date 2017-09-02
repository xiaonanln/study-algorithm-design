
gaps = (701, 301, 132, 57, 23, 10, 4, 1)

class ShellSort(object):
	def __init__(self, list):
		self.list = list

	def sort(self):
		for gap in gaps:
			insertionSortWithGap( self.list, gap )

def insertionSortWithGap(list, gap):
	N = len(list)
	for i in xrange(1, N, gap):
		# move i to proper position
		iv = list[i]
		ii = i
		while ii > 0 and iv < list[ii - 1]:
			list[ii] = list[ii - 1]
			ii -= 1

		list[ii] = iv

