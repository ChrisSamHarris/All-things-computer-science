# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2


class MinStack(object):

    def __init__(self):
        self.stack = []

        # cant just keep track of a value as when that value gets popped - the minValue will no longer be valid 
        self.min_stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        
        # populating min_stack for the first time | OR | value is less than min_stack 
        if not self.min_stack or val < self.min_stack[-1]:
            self.min_stack.append(val)
        # replicate the existing min_stack item - keeping track of the min_value at that time  
        else:
            self.min_stack.append(self.min_stack[-1])
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack = self.stack[:-1]
        self.min_stack = self.min_stack[:-1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        Requires keeping track of the minimum value throughout the class
        """
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

