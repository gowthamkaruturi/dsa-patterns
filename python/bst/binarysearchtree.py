import Node

class BST:
    def __init__(self, val):
        self.root = Node.Node(val)

    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
    def search(self, val):
    
        if self.root == val:
            return True
        else:
            self.root.search(val)
            
    def delete(self,val):
        return self.root.delete(val=val)
            
    def preOrderTraversal(self,root:Node.Node):
        if root:
            print(root.val)
            self.preOrderTraversal(root.leftChild)
            self.preOrderTraversal(root.rightChild)

    def preOrderTraversalIterative(self, root:Node.Node):
        stack = [root]
        result = []     
        while stack:
            tmp = stack.pop()
            if tmp:
                result.append(tmp.val)
                if tmp.right:
                    stack.append(tmp.right)
                if tmp.left:
                    stack.append(tmp.left)
        return result

    def inorderTraversal(self, root:Node.Node):
        if root:
            self.inorderTraversal(root.leftChild)
            print(self.val)
            self.inorderTraversal(root.rightChild)

    def inorderTraversaliterative(self, root:Node.Node):
        current = root
        stack , result = [],[]
       
        while current and stack:
            while current:
                stack.append(current)
                current = current.leftChild
            current = stack.pop()
            result.append(current)
            current = current.right   
        return result


