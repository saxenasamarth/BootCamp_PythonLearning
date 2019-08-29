'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack():
	def __init__(self):
		self.stack = []
		self.min_stack = []
		self.min_value = None
	
	def push(self, val):
		self.stack.append(val)
		if self.min_value == None:
			self.min_value = val
		else:
			if self.min_value > val:
				self.min_value = val
		self.min_stack.append(self.min_value)

	def pop(self):
		val = self.stack.pop()
		self.min_stack.pop()
		if len(self.min_stack) > 0:
			self.min_value = self.min_stack[-1]
		else:
			self.min_value = None
		return val	

	def top(self):
		return self.stack[-1]
		
	def getMin(self):
		return self.min_stack[-1]
		
s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)
print(s.getMin())
print(s.pop())
print(s.top())		
print(s.getMin())