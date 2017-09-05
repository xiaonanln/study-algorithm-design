
import Heap

class PriorityQueue(object):
	def __init__(self, N):
		# self.prio = [None] * N
		self.idx = [-1] * N
		self.heap = []

	def push(self, n, prio):
		assert self.idx[n] == -1, (n, self.idx[n])
		self.heap.append((-prio, n))
		self.idx[n] = len(self.heap) - 1

		self.moveup(len(self.heap) - 1)

	def pop(self):
		minval = self.heap[0]
		n = minval[1]

		if len(self.heap) > 1:
			self.heap[0] = self.heap.pop()
			self.idx[n] = -1
			self.idx[self.heap[0][1]] = 0

			self.movedown(0)
		else:
			self.heap.pop()
			self.idx[n] = -1

		return n

	def __contains__(self, n):
		return self.idx[n] != -1

	def __len__(self):
		return len(self.heap)

	def peek(self):
		return self.heap[0][1]

	def change(self, n, prio):
		idx = self.idx[n]
		assert idx != -1, (n, idx)

		oldPrio = -self.heap[idx][0]
		self.heap[idx] = (-prio, self.heap[idx][1])
		if prio > oldPrio:
			self.moveup(idx)
		elif prio < oldPrio:
			self.movedown(idx)

	def moveup(self, i):
		item = self.heap[i]
		n = item[1]
		pi = (i + 1) // 2 - 1
		while i > 0 and item < self.heap[pi]:
			self.heap[i] = self.heap[pi]
			self.idx[self.heap[i][1]] = i
			i = pi
			pi = (i + 1) // 2 - 1

		self.heap[i] = item
		self.idx[n] = i

	def movedown(self, i):
		length = len(self.heap)
		item = self.heap[i]
		n = item[1]

		while True:
			c = (i+1) * 2 -1
			if c >= length:
				break

			if c+1 < length and self.heap[c+1] < self.heap[c]:
				c += 1

			if self.heap[c] >= item:
				break

			self.heap[i] = self.heap[c]
			self.idx[self.heap[i][1]] = i
			i = c

		self.heap[i] = item
		self.idx[n] = i

if __name__ == '__main__':
	pq = PriorityQueue(3)
	pq.push(0, 100)
	pq.push(1, 200)
	pq.push(2, 300)
	assert pq.pop() == 2
	assert pq.pop() == 1
	assert pq.pop() == 0

	pq.push(0, 100)
	pq.push(1, 200)
	pq.push(2, 300)
	pq.change(1, 50)
	assert pq.pop() == 2
	assert pq.pop() == 0
	assert pq.pop() == 1

	import random
	pq = PriorityQueue(100)
	# inpq = {}
	for i in xrange(100000):
		if len(pq) == 0 or random.random() < 0.7:
			n = random.randint(0, 99)
			prio = random.randint(1, 10000)
			if n in pq:
				pq.change(n, prio)
			else:
				pq.push(n, prio)

		else:
			n = pq.pop()

