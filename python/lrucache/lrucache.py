class Node():
  def __init__(self, key=0,val=0):
    self.key, self.val = key,val
    #ref pointer of last and first to be none
    self.prev =self.next = None

class LRUCache():
  
  def __init__(self, capacity :int):
    self.capacity = capacity 
    self.cache = {}
    self.left , self.right = Node(), Node()
    self.left.next ,self.right.prev = self.right, self.left
  
  def get(self, key:int) -> int:
    if key in self.cache:
      # when it exists remove and reinsert at the tail or right
      self.remove(self.cache[key])
      self.insert(self.cache[key])
      return self.cache[key].val
    return -1
  
  def remove(self, node:Node):
    l = node.prev
    r = node.next
    l.next= r
    l.prev =l
  
  def insert(self, node:Node):
    last = self.right.prev
    last.next = node
    node.next = self.right
    node.prev = last
    self.right.prev = node
    
      
  def put(self, key:int, value:int) ->None:
    if key in self.cache:
      self.remove(self.cache[key])
    self.cache[key]= Node(key=key,val=value)
    self.insert(self.cache[key])
    if len(self.cache) > self.capacity:
      lru = self.left.next
      self.remove(lru)
      del self.cache[lru.key]
        

from collections import OrderedDict
class LRUCacheOrderedDict():
  
  def __init__(self,capacity):
    self.capacity =capacity
    self.cache = OrderedDict()
    
  def get(self, key:int) -> int:
    if key in self.cache:
      # when it exists remove and reinsert at the tail or right
      self.cache.move_to_end(key=key)
      return self.cache[key]
    return -1
    
  def put(self, key: int, value: int) -> None:
    self.cache[key] = value
    self.cache.move_to_end(key)
    if len(self.cache) > self.capacity:
        self.cache.popitem(last = False)


# 1,2,3

# 4

# 1,2,3,4
# None -->1-->2-->3-->None
# l None <--1<--2<--3<--None r

# last = right.prev
# last.next= Node
# node.next = self.right
# node.prev= last


# inserting an element  for the first time
# self.cache = {Node()}


if __name__ == "__main__":
  cache = LRUCache(3)
  cache.put(1,1)
  print(cache)
  cache.put(3,3)
  print(cache)
  cache.put(3,3)
  print(cache)
  cache.put(4,4)
  print(cache)