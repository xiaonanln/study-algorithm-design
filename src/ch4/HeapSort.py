
class HeapSort(object):
	def __init__(self, list):
		self.list = list

	def sort(self):
		list = self.list
		self.heapify(list)
		for i in xrange(len(self.list)-1, 0, -1): # from len(list) ~ 1
			list[i], list[0] = list[0], list[i] # swap list[i] and list[0]
			HeapSort.movedown(list, 0, i)

	@staticmethod
	def heapify(list): # convert list to max heap
		length = len(list)
		for i in xrange(len(list) - 1, -1, -1):  # len(list)-1 ~ 0
			HeapSort.movedown(list, i, length)

	@staticmethod
	def movedown(list, i, length):
		val = list[i]
		while True:
			c = (i + 1) * 2 - 1
			if c >= length:
				break

			if c + 1 < length and list[c + 1] > list[c]:
				c += 1

			if list[c] <= val:
				break

			list[i] = list[c]
			i = c

		list[i] = val
