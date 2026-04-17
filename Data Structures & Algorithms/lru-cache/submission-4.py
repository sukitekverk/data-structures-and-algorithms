class Node:
    def __init__(self, key: int,value:int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}
        
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.prev = self.tail
        self.tail.next = self.head

    
    def remove(self, node:Node):
        node.prev.next = node.next
        node.next.prev = node.prev

        ## two open pointers coming from removed one
   
        
    def add(self, node:Node):
        node.next = self.head
        node.prev=self.head.prev
        self.head.prev.next = node
        self.head.prev = node
          

    def get(self, key: int) -> int:
        if key in self.keys:
            node = self.keys[key]
            self.remove(node)
            self.add(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.remove(self.keys[key])
       
        self.keys[key]= Node(key,value)
        self.add(self.keys[key])

        if len(self.keys)>self.capacity: ## at capacity
            lru =  self.tail.next
            self.remove(lru)
            del self.keys[lru.key]
       


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)