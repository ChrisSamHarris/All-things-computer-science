#### Add to the stack 
def push(self, n):
    # using the pushback function from dynamic arrays to add to the stack
    self.stack.append(n)
    
#### Pop from the stack
def pop(self):
    return self.stack.pop()


#### Peek at the top of the stack
def peek(self):
    return self.stack[-1]
