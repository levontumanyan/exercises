"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""

"""
Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack print(minStack = new MinStack();
print(minStack.push(-2);
print(minStack.push(0);
print(minStack.push(-3);
print(minStack.getMin(); // return -3
print(minStack.pop();
print(minStack.top();    // return 0
print(minStack.getMin(); // return -2
"""

class MinStack():

	def __init__(self):
		self.main_stack = []
		self.min_stack = []

	def push(self, val: int) -> None:
		self.main_stack.append(val)
		
		if not self.min_stack or val <= self.min_stack[-1]:
			self.min_stack.append(val)

	def pop(self) -> None:
		popped = self.main_stack.pop()

		if popped == self.min_stack[-1]:
			self.min_stack.pop()

	def top(self) -> int:
		return self.main_stack[-1]

	def getMin(self) -> int:
		return self.min_stack[-1]

minStack = MinStack()

print(minStack.push(-2))
print(minStack.push(0))
print(minStack.push(-3))
print(minStack.push(4))
print(minStack.push(5))
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())

"""
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

[-2, 0, -3, 4, 5, 2, -5] get min [-3]
main_stack = [-2, 0, -3, 4, 5, 2]
min_stack = [5, 4, 0, -2, -3]



"""