class MergeSort(object):
	def __init__(self, list):
		self.list = list

	def sort(self):
		aux = [0 for _ in self.list]
		mergesort(self.list, 0, len(self.list), aux)

def mergesort(list, l, h, aux):
	if h <= l+1:
		return

	mid = (l+h)//2
	mergesort(list, l, mid, aux)
	mergesort(list, mid, h, aux)
	merge(list, l, mid, h, aux)

def merge(list, l, m, h, aux):
	aux[l:h] = list[l:h] # copy all items to aux
	w = l
	r1, r2 = l, m
	while r1 < m and r2 < h:
		if aux[r1] <= aux[r2]:
			list[w] = aux[r1]
			r1 += 1
		else:
			list[w] = aux[r2]
			r2 += 1

		w += 1

	while r1 < m:
		list[w] = aux[r1]
		w += 1
		r1 += 1
