class MyStack:

    def __init__(self):
        self.front_queue = []
        self.back_queue = []
        

    def push(self, x: int) -> None:
        self.front_queue.append(x)
        

    def pop(self) -> int:
        return self.front_queue.pop() 

    def top(self) -> int:
        return self.front_queue[-1]

        

    def empty(self) -> bool:
        if self.front_queue: return False
        else: return True
        
#This was the right way on doing this.
"""
from collections import deque

class MyStack:

    def __init__(self):
        # Initialize an empty queue
        self.q = deque()

    def push(self, x: int) -> None:
        # Add new element
        self.q.append(x)
        # Rotate the queue so that x becomes the front (top of stack)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # Remove and return the front element (top of stack)
        return self.q.popleft()

    def top(self) -> int:
        # Peek at the front element
        return self.q[0]

    def empty(self) -> bool:
        # Check if queue is empty
        return not self.q
"""

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()