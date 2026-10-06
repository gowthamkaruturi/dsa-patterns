from collections import deque
from typing import Optional,List
#from graphs.graph import TrieNode


class TreeNode:
  def __init__(self, val=0,left=0,right=0):
    self.val= val
    self.left = left
    self.right= right
  
  def getVal(self):
    return self.val
  
  def setLeft(self, node:TrieNode):
    self.left = node
   
class Trees:
  def swap(self, root:TreeNode):
    if root is None:
      return 
    temp = root.left
    root.left=root.right
    root.right= temp
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    self.invertTree(root.left)
    self.invertTree(root.right)
    root.left, root.right = root.right,root.left
  
    return root
  def invertBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
      return 
    dq = deque()
    dq.append(root)
 
    while dq:
      curr = dq.popleft()
      self.swap(curr)
      if curr.left:
        dq.append(curr.left)
      if curr.right:
        dq.append(curr.right)
   
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      if p is None and q is None:
          return True
      if p and q:
          return (p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
      return False
    
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #level order and preorder 
    #double eneded
    queue = deque()
    queue.append(root)
    ans = []
    if root:
        result = []
        while queue:  
            temp = []
            for i in range(len(queue)):
                popped = queue.popleft()
                if popped:
                    temp.append(popped.val)
                    if popped.left:
                        queue.append(popped.left)
                    if popped.right:
                        queue.append(popped.right)
            result.append(temp)

        for vals in result:
            ans.append(vals[-1])     
    return ans
  
  
  def numIslands(self, grid: List[List[str]]) -> int:
    m = len(grid[0])
    n = len(grid)

    count =0
    for i in range(n):
        for j in range(m):
            if grid[i][j] =="1":
                count+=1
                self.dfs(i,j,grid)

    return count
    
  def dfs(self,i,j,grid):
      if i not in range(len(grid)) or j not in range(len(grid[0])) or grid[i][j]=="0":
          return 

      grid[i][j]="0"
      self.dfs(i+1,j,grid)
      self.dfs(i-1,j,grid)
      self.dfs(i,j+1,grid)
      self.dfs(i,j-1,grid)

  def isValidBST(self, root: Optional[TreeNode]) -> bool:
      if not root:
          return True
      stack =[(root,-float('inf'),float('inf'))]
      while(len(stack)):
          node, minimum, maximum = stack.pop()
          
          if node.val <= minimum or node.val >= maximum:
              return False
          if node.left:
              stack.append((node.left, minimum, node.val))
          if node.right:
              stack.append((node.right,node.val,maximum))
      return True