class NodeList:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next


class Hashmap:
    def __init__(self):
        self.map = [NodeList() for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        curr = self.map[key % len(self.map)]
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next
        curr.next = NodeList(key, value)

    def get(self, key: int) -> int:
        curr = self.map[key % len(self.map)].next
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1
    
    def remove(self, key: int) -> None:
        curr = self.map[key % len(self.map)]
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


hashmap = Hashmap()

hashmap.put(1, 10)
hashmap.put(2, 20)
hashmap.put(3, 30)

assert hashmap.get(1) == 10
assert hashmap.get(2) == 20
assert hashmap.get(3) == 30

hashmap.put(1002, 25)
assert hashmap.get(1002) == 25

hashmap.remove(1)
assert hashmap.get(1) == -1

assert hashmap.get(5) == -1

print("All tests passed!")