class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache ={}
        self.head=Node()
        self.tail =Node()
        self.head.next=self.tail
        self.tail.prev = self.head
    
    def _remove(self,node):
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node

    def _add_to_head(self, node):
        node.next = self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node= self.cache[key]
            node.value=value
            self._remove(node)
            self._add_to_head(node)
        else:
            new_node=Node(key,value)
            self.cache[key]=new_node
            self._add_to_head(new_node)
            if len(self.cache)>self.capacity:
                lru_node=self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
