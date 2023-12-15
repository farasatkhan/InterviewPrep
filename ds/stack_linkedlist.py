class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__ (self):
        self.head = None

    def push(self, data) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def pop(self) -> int:
        prev = None
        current = self.head
        while current.next:
            prev = current
            current = current.next
        current = None
        prev.next = None
    
    def display(self) -> None:
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
    
    def peek(self, key) -> bool:
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    def isEmpty(self) -> bool:
        return True if not self.head else False
    
    def size(self) -> int:
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        
        return size
    

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
stack.display()
print(stack.peek(3))
print(stack.isEmpty())
print(stack.size())