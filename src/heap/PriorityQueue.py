
import Heap

class PriorityQueue(object):
	def __init__(self):
		self.items = []

	def push(self, item, prio):
		Heap.Push(self.items, (-prio, item))

	def pop(self):
		top = Heap.Pop(self.items)
		return top[1]

	def peek(self):
		return self.items[0][1]

	def set(self, item, prio):
		pass

if __name__ == '__main__':
	pq = PriorityQueue()
	pq.push(1, 1)
	pq.push(2, 3)
	pq.push(3, 2)
	assert pq.pop() == 2
	assert pq.pop() == 3
	assert pq.pop() == 1

