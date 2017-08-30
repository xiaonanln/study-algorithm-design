import random

class QuickSort (object):
	def __init__(self, list):
		self.list = list

	def sort(self):
		shuffle(self.list)
		quicksort(self.list, 0, len(self.list))

def shuffle(list):
	N = len(list)
	for i in xrange(0, N-1):
		# move i to randomly i+1 ~ len(list)-1
		r = random.randint(i+1, N-1)
		list[i], list[r] = list[r], list[i]

def quicksort(list, l, h):
	if h <= l+1:
		return


	pivot = list[h-1]
	firsthigh = l
	for i in xrange(l, h-1):
		if list[i] < pivot:
			list[i], list[firsthigh] = list[firsthigh], list[i]
			firsthigh += 1

	list[h-1], list[firsthigh] = list[firsthigh], list[h-1]

	# print firsthigh-l, h-firsthigh-1, '|',
	# print list[l:firsthigh], list[firsthigh], list[firsthigh+1:]
	quicksort(list, l, firsthigh)
	quicksort(list, firsthigh+1, h)

if __name__ == '__main__':
	list = range(100)
	shuffle(list)
	print list
	quicksort(list, 0, len(list))
	print list