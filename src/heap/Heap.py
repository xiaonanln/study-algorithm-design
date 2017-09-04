
def Heapify(list):
	for i in xrange(len(list)-1, -1, -1): # len(list)-1 ~ 0
		movedown(list, i)

def Pop(heap):
	minval = heap[0]
	if len(heap) > 1:
		heap[0] = heap.pop()
		movedown(heap, 0)
	else:
		heap.pop()

	return minval

def Push(heap, val):
	heap.append(val)
	moveup(heap, len(heap)-1)

def moveup(list, i):
	val = list[i]
	pi = (i + 1) // 2 - 1
	while i > 0 and val < list[pi]:
		list[i] = list[pi]
		i = pi
		pi = (i + 1) // 2 - 1

	list[i] = val

def movedown(list, i):
	length = len(list)
	val = list[i]
	while True:
		c = (i+1) * 2 -1
		if c >= length:
			break

		if c+1 < length and list[c+1] < list[c]:
			c += 1

		if list[c] >= val:
			break

		list[i] = list[c]
		i = c

	list[i] = val
