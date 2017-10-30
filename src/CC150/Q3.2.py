
# How would you design a stack which, in addition to push and pop,
# also has a function min which returns the minimum element?
# Push, pop and min should all operate in O(1) time.


class MinStack(object):
	def __init__(self):
		self.stack = []
		self.mins = []

	def push(self, val):
		self.stack.append(val)
		if not self.mins or val <= self.mins[-1]:
			self.mins.append( val )

	def pop(self):
		val = self.stack.pop()
		if val == self.mins[-1]:
			self.mins.pop()

		return val

	def min(self):
		return self.mins[-1]



ms = MinStack()
ms.push(10)
assert ms.min() == 10
ms.push(9)
assert ms.min() == 9
ms.push(11)
assert ms.min() == 9
ms.push(9)
assert ms.min() == 9
ms.push(8)
assert ms.min() == 8
assert ms.pop() == 8
assert ms.min() == 9
assert ms.pop() == 9
assert ms.min() == 9
assert ms.pop() == 11
assert ms.min() == 9
assert ms.pop() == 9
assert ms.min() == 10
assert ms.pop() == 10