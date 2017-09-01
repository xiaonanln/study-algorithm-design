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

	# print l, h

	pivot = list[h-1]
	sm, la = l, h-2
	while True:
		while list[sm] < pivot:
			sm += 1

		while la >= 0 and list[la] >= pivot:
			la -= 1

		if sm > la:
			break

		list[la], list[sm] = list[sm], list[la]
		sm += 1
		la -= 1

	list[sm], list[h-1] = list[h-1], list[sm]
	quicksort(list, l, sm)
	quicksort(list, sm+1, h)


if __name__ == '__main__':
	list = range(100)
	shuffle(list)
	print list
	quicksort(list, 0, len(list))
	print list