#!/usr/bin/python3

List = list

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.capacity = 0
        self.head = Node(None, None) 
        self.tail = Node(None, None) 
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next, node.prev = None, None
          
    def add(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node 
             

    def get(self, key: int) -> int:
               
        found = self.cache.get(key, None)
               
        if not found:
            return -1
                 
        self.remove(found)
        self.add(found)
                  
        return found.value 
                  

    def put(self, key: int, value: int) -> None:
                   
        node = Node(key, value)
        found = self.get(key)
                    
        if found == -1:
            self.add(node)
            self.cache[node.key] = node
            self.capacity += 1
        else:
            self.head.next.value = value
                         
        if self.capacity > self.max_capacity:
            self.capacity -= 1
            del self.cache[self.tail.prev.key]
            self.remove(self.tail.prev)

def test_case(actions, values):
    if len(actions) != len(values):
        return 0

    lru = None
    ans = []
    for i in range(len(actions)):
        action = actions[i]
        value = values[i]
        if action == "LRUCache":
            lru = LRUCache(values[i][0])
            ans.append(None)
        elif action == "get":
            ans.append(lru.get(values[i][0]))
        elif action == "put":
            ans.append(None)
            lru.put(values[i][0], values[i][1])
    return ans




if __name__ == "__main__":
    actions = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    print(test_case(actions, values))

