from typing import List


class solution:
    def solve(self, board: List[List[str]]) -> None:
      """
      Do not return anything, modify board in-place instead.
      """
      rows = len(board)
      cols = len(board[0])
      for i in range(rows):
          for j in range(cols):
              if i ==0 or  j == cols -1 or i==rows-1 or j==0:
                  if board[i][j]=="O":
                      self.dfs(i,j,board)
      for i in range(rows):
          for j in range(cols):
              if  board[i][j]=="T":
                  board[i][j]="O"
              else:
                  board[i][j]="X"    


    def dfs(self,i,j,board):
        if i not in range(len(board)) or j not in range(len(board[0])) or board[i][j]!="O":
          return 

        board[i][j]="T"
        self.dfs(i+1,j,board)
        self.dfs(i-1,j,board)
        self.dfs(i,j+1,board)
        self.dfs(i,j-1,board)


class TrieNode:
    def _init_(self):
        self.children = {}
        self.end = False

class Trie:

    def _init_(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root

        for ch in word:
            if ch not in temp.children:
                temp.children[ch] = TrieNode()
            temp = temp.children[ch]

        temp.end = True
            


    def search(self, word: str) -> bool:
        temp = self.root

        for ch in word:

            if not temp.children[ch]:
                return False
            temp = temp.children[ch]

        return True if temp.end == True else False 



    def startsWith(self, prefix: str) -> bool:
        temp = self.root

        for ch in prefix:
        
            if not temp.children[ch]:
                return False

            temp = temp.children[ch]

        return True 
        
