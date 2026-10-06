class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

        
    def isempty(self):
        # Check if the node is empty (value is None)
        return (self.val == None)
    def isleaf(self):
        if self.rightChild == None and self.leftChild ==None :
            return True
        else:
            return False
    def maxval(self):
        if self.rightChild.rightChild == None:
            return self.rightChild 
        else:
            self.rightChild.maxval()
    def insert(self, val):
        if val < self.val:
            if self.leftChild:
                self.leftChild.insert(val)
            else:
                self.leftChild = Node(val)
                return
        else:
            if self.rightChild:
                self.rightChild.insert(val)
            else:
                self.rightChild = Node(val)
                return
    def search(self, val):
        if val == self.val:
            return True
        elif val < self.val:
           if not self.leftChild:
               return False
           else:
               self.leftChild.search(val=val)
        else:
            if not self.rightChild:
                return False
            else:
                self.rightChild.search(val=val)
    def delete(self,val ):
        if self.isempty():
            return None
        if val < self.val:
            self.leftChild.delete(val)
            return 
        if val > self.val:
            self.rightChild.delete(val)
            return 
        if self.val == val:
            if self.isleaf():
                self.val = None
                self.leftChild= None
                self.rightChild= None
            elif self.leftChild.isempty():
                self.val = self.rightChild.val
                self.leftChild= self.rightChild.leftChild
                self.rightChild= self.rightChild.rightChild
                return 
            else:
                self.val = self.leftChild.maxval()
                self.leftChild.delete(self.leftChild.maxval)
                return 

