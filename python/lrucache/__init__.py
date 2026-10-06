from collections import OrderedDict
class Node():
  def __init__(self, key,val):
    self.key, self.val = key,val
    self.prev = self.next = None

class LRUCache():
  
  def __init__(self, capacity :int):
    self.capacity = capacity
    
    self.cache = {}
    self.left , self.right = Node(0), Node(0)
  
  def get(self, key:int) -> int:
    if key in self.cache:
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
    self.insert(self.cache)
    if len(self.cache) > self.capacity:
      lru = self.left.next
      self.remove(lru)
      del self.cache[lru.key]