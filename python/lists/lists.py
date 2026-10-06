class ListAlgo:

  def __init__(self):
    
    self.items =[]
  
  
  def Append(self, element:int):
    self.items.append(element)
  
  def Pop(self) -> int:
    return self.items.pop()
  
  def RemoveEvent(self, lst:list)->list:
    return  [item for item in lst if item % 2 !=0 ]

  def merge_lists(lst:list, lst2:list) -> list:
    return []
  

if __name__ == "__main__":
  listAlgo = ListAlgo()
  print(listAlgo.RemoveEvent([2,3,5,6,8]))
  