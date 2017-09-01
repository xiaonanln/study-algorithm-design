import random

class QuickSortW3 (object):
	def __init__(self, list):
		self.list = list

	def sort(self):
		shuffle(self.list)
		quicksort_w3(self.list, 0, len(self.list))

def shuffle(list):
	N = len(list)
	for i in xrange(0, N-1):
		# move i to randomly i+1 ~ len(list)-1
		r = random.randint(i+1, N-1)
		list[i], list[r] = list[r], list[i]

def quicksort_w3(list, l, h):
	if h <= l+1:
		return

	pivot = list[h-1]
	eq, la = l, l
	# print list
	for i in xrange(l, h-1):
		if list[i] > pivot:
			pass
		elif list[i] < pivot:
			if eq < i:
				list[eq], list[i] = list[i], list[eq]
				if la > eq:
					list[la], list[i] = list[i], list[la]

			eq += 1
			la += 1
		else: # list[i] == pivot
			list[la], list[i] = list[i], list[la]
			la += 1

		# print '> ',list[l:eq], list[eq:la], list[la:]

	list[la], list[h-1] = list[h-1], list[la]
	la += 1
	# print list[l:eq], list[eq:la], list[la:]
	quicksort_w3(list, l, eq)
	quicksort_w3(list, la, h)

if __name__ == '__main__':
	list = [1, 3, 0, 4, 2]
	quicksort_w3(list, 0, len(list))
	print list