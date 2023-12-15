class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data) -> None:
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self) -> None:
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def search(self, key) -> bool:
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    def delete(self, key) -> None:
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None


linkedList = LinkedList()
linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
linkedList.append(4)
linkedList.append(5)
linkedList.append(6)
linkedList.display()
print(linkedList.search(4))
linkedList.delete(1)
linkedList.delete(5)
linkedList.delete(6)
linkedList.display()