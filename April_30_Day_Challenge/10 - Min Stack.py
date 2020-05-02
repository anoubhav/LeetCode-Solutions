# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3292/


# The insight is to keep track of the minimum value so far and push it, along with the number we are pushing, onto the stack.

class MinStack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        m = x
        if self.stack:
            m= self.stack[-1][1]
            if m > x: 
                m = x
        self.stack.append((x, m))
                
    def pop(self):
        if len(self.stack):
            temp = self.stack.pop()
            return temp[0]
    
    def top(self):
        if len(self.stack):
            return self.stack[-1][0]

    def getMin(self):
        if len(self.stack):
            return self.stack[-1][1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin() )  #--> Returns -3.
print(minStack.pop())
print(minStack.top())      #--> Returns 0.
print(minStack.getMin())   #--> Returns -2.

