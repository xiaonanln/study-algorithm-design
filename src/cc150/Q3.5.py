# Implement a MyQueue class which implements a queue using two stacks.


class Queue(object):
	def __init__(self):
		self.s1 = []
		self.s2 = []

	def push(self, val):
		self.s1.append(val)

	def popleft(self):
		if not self.s2:
			while self.s1:
				self.s2.append(self.s1.pop())

		return self.s2.pop()


q = Queue()
q.push(1)
q.push(2)
q.push(3)
print q.popleft()
q.push(4)
print q.popleft()
print q.popleft()
print q.popleft()

