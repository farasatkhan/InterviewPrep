from typing import List

class Stack:
    def __init__ (self):
        self.stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

    def pop(self) -> None:
        self.stack.pop() if self.stack else None

    def get(self) -> int:
        return self.stack[-1]
    
    def print(self) -> List[int]:
        return self.stack
    

stack = Stack()
stack.push(10)
stack.push(9)
stack.push(8)
stack.push(7)
stack.pop()
print(stack.print())