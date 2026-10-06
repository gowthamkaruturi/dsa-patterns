from typing import Optional


class MinHeap:
  def __init__(self):
    self.nodes =[]
  
  def __len__(self):
    return len(self.nodes)
  
  def __get_left_child_index(self, parent_index:int) -> int:
    if self.__len__() > 2*parent_index+1:
       return 2*parent_index+1
    return -1
    
  
  def __get_right_child_index(self,parent_index:int) -> int:
    
    if self.__len__() > 2*parent_index+2:
      return 2*parent_index+2
    return -1
  
  def __get_parent_index(self, child_index:int) -> int:
    
    return (child_index-1)//2
  
  def __isleaf(self,pos):
    return pos*2 > self.__len__()
  
  def __swap(self,left, right):
      self.nodes[left],self.nodes[right]=self.nodes[right],self.nodes[left]
  def __heapify(self, root:Optional[int]=None):
    
    if not self.__isleaf(root):
    
      if (self.__get_left_child_index(root)>=0 and self.nodes[root]> self.nodes[self.__get_left_child_index(root)]) or (self.__get_right_child_index(root)>=0 and self.nodes[root]> self.nodes[self.__get_right_child_index(root)]):
        if self.nodes[self.__get_left_child_index(root)] < self.nodes[self.__get_right_child_index(root)]:
          self.__swap(root,self.__get_left_child_index(root))
          self.__heapify(self.__get_left_child_index(root))
        else:
          self.__swap(self,self.__get_right_child_index(root))
          self.__heapify(self.__get_right_child_index(root))
          
          
  def __build_heap(self):
    for index in range(self.__len__(),-1,-1):
      self.__heapify(index)
  
  def PreOrder(self,root):
    if root ==-1:
      return 
    print("{"+str(self.nodes[root])+"}")
    self.PreOrder(self.__get_left_child_index(root))
    self.PreOrder(self.__get_right_child_index(root))
    
  def Print(self):
    
    self.PreOrder(0)
    
    # for i in range(1, (self.__len__()//2)+1):
    #   print("parant:"+ str(self.nodes[i])+ "left child" +str(self.nodes[2*i]) +"right child" + str(self.nodes[2*i+2]))
    
  def insert(self,element):
    self.nodes.append(element)
    
    current_index = self.__len__()-1
    while self.__get_parent_index(child_index=current_index) >=0 and self.nodes[current_index] < self.nodes[self.__get_parent_index(child_index=current_index)] :
      self.__swap(current_index,self.__get_parent_index(current_index))
      current_index = self.__get_parent_index(current_index)
    
if __name__ == "__main__":
  Heap = MinHeap()
  Heap.insert(27)
  Heap.insert(18)
  Heap.insert(9)
  Heap.insert(3)
  Heap.insert(0)
  Heap.insert(-3)
  print(Heap.nodes)
  Heap.Print()
        _3
     3      0
27      9 18