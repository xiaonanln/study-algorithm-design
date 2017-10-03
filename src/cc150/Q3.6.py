# Write a program to sort a stack in ascending order. You should not make any assumptions about how the stack is implemented. The following are the only functions that should be used to write this program: push | pop | peek | isEmpty.

class Stack(list):
	def push(self, val):
		self.append(val)

	# pop == list.pop

	def isEmpty(self):
		return not self

	def peek(self):
		return self[-1]


def sortStack(stack):
	pass

stack = Stack()
import random
for i in xrange(100):
	stack.push(random.randint(1, 100))

sortStack(stack)
while not stack.isEmpty():
	print stack.pop()

