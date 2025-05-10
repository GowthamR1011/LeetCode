class ListNode:
    def __init__(self,key, val,next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity 
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        head, nxt = self.head, self.head.next
        head.next =  nxt.prev  = node
        node.next, node.prev = nxt, head

    def remove(self,node):
        prev , nxt = node.prev,node.next
        prev.next, nxt.prev = nxt, prev 


    def get(self, key: int) -> int:
        
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = ListNode(key,value)
        self.insert(self.cache[key])

        if len(self.cache) >  self.capacity:
            rm = self.tail.prev

            self.cache.pop(rm.key)
            self.remove(rm)

        

        




