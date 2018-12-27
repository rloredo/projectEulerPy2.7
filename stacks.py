class stack:

	def __init__(self):
		self.stack = []

	def pile(self, x):
		self.stack.append(x)

	def empty(self):
		return len(self.stack) == 0

	def top(self):
		return self.stack[len(self.stack)-1]

	def unpile(self):
		self.stack.pop()
