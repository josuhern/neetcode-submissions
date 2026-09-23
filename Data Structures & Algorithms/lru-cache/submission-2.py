class Node:
    def __init__(self, key:int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.start = Node(0,0)
        self.end = Node(0,0)
        self.start.next = self.end
        self.end.prev = self.start
        self.hashMap = {}
        self.cap = capacity

    def remove(self, node) -> None:
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def insert(self, node) -> None:
        prevNode = self.end.prev
        nextNode = self.end
        prevNode.next = node
        nextNode.prev = node
        node.prev = prevNode
        node.next = nextNode

    def get(self, key: int) -> int:
        if key in self.hashMap:            
            curr = self.hashMap[key]
            self.remove(curr)
            self.insert(curr)
            return curr.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            curr = self.hashMap[key]
            self.remove(curr)
        newNode = Node(key, value)
        self.hashMap[key] = newNode
        self.insert(newNode)

        if(len(self.hashMap)>self.cap):
            extra = self.start.next
            self.remove(extra)
            del self.hashMap[extra.key]
