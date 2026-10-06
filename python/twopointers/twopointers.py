from typing import List
class TwoPointers(object):
  
  def isPallindrome(self, s :str) -> bool:
    s = str.lower(''.join(e for e in s if e.isalnum()))
    
    left,right =0,len(s)-1
    while left < right:
      if s[left] != s[right]:
        return False
      left +=1
      right -=1
    return True
  
  def threeSum(self, nums: List[int]) -> List[List[int]]:
      res = set()
      n, p, z = [],[],[]
      for num in nums:
          if num >0: 
              p.append(num)
          elif num <0:
              n.append(num)
          else:
              z.append(num)       
    
      N,P= set(n),set(p)
      if z:
          for num in p:
              if -1*num in n:
                  res.add((-1*num,0,num))

      if len(z)>=3:
          res.add((0,0,0))           
      
      for i in range(len(n)):
          for j in range(i+1, len(n)):
              target = -1*(n[i]+n[j])
              if target in P:
                  res.add(tuple(sorted([n[i],n[j],target])))


      for i in range(len(p)):
          for j in range(i+1, len(p)):
              target = -1*(p[i]+p[j])
              if target in N:
                  res.add(tuple(sorted([p[i],p[j],target])))            
      return res

  def maxArea(self, height: List[int]) -> int:
    maxArea =0
    left, right =0,len(height)-1
    while(left<right):
        maxArea = max(maxArea, min(height[left],height[right])*(right-left))
        if height[left]< height[right]:
            left += 1
        else:
            right -= 1
    return maxArea
  
  
if __name__ == "__main__":
  sol = TwoPointers()
  sol.isPallindrome("A man, a plan, a canal: Panama")
  sol.threeSum()