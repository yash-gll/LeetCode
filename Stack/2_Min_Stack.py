""" Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function. """

"""
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.output = []
        self.curr_min = []

    def push(self, val):
        self.stack.append(val)
        if not self.curr_min or val <= self.curr_min[-1]:
            self.curr_min.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.curr_min[-1]:
            self.curr_min.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.curr_min[-1]