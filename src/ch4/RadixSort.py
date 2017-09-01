
class RadixSort(object):
	def __init__(self, list):
		self.list = list

	def sort(self):
		maxdiv = 1
		for n in self.list:
			if n > maxdiv:
				maxdiv *= 10

		lists = [self.list]

		div = 1
		while div <= maxdiv:
			buckets = [[] for _ in xrange(10)]
			for list in lists:
				for n in list:
					d = (n // div) % 10
					buckets[d].append(n)
			div *= 10

			lists = buckets

		self.list[:] = [n for list in lists for n in list]


if __name__ == '__main__':
	list = [1,2,100,200,3,4]
	RadixSort(list).sort()
	print list


