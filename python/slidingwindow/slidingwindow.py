class Solution(object):
  
  from typing import List
  def maxArea(self, height:List[int]) -> int:
    area =0
    left =0
    right = len(height)-1
    while left < right :
      shortestLine = min(height[left],height[right])
      area = max(area, shortestLine*(right-left))
      if height[right]<height[left]:
        left +=1
      else:
        right -=1
    return area
    
  def lengthOfLongestSubstring(self, s: str) -> int:
    # always check for the length of the str if zero return zero
    if len(s) ==0:
        return 0
    #initialize left ptr, right ptr , maximumlength, seen map to following values
    # 0,1,0,1
    # iterate the string until it reaches starting with right ptr =1 as left ptr already holds the zero ptr
    # check if the right ptr being interated is already present in the dict.
    # if it is present in the dict shift the left operator to the index where the seen value is present
    # calculate the max length always to update the maxlength to see if the maxlength is calculated.
    # always the update the seen value from right ppointer 
    left, right ,maximumLength, seen = 0,0,0,{}
    while right < len(s):
      if s[right] in seen:
          left = seen[s[right]]+1
      maximumLength = max(maximumLength, right-left+1)
      seen[s[right]]=right
      right +=1 
    return maximumLength
  
  
  def characterReplacement(self, s:str, k:int) -> int:
    count = {}
    result = 0
    left =0
    for right in range(len(s)):
      count[s[right]] = 1+ count.get(s[right],0)
      if (right-left+1) -max(count.values) >k:
        count[s[left]] -= 1
        left += 1 
      result = max(result , right-left+1)
      return result       
    
  def maxProfit(self, prices:List[int]) -> int:
    maxProfit =0
    left =0
    right =1
    while right < len(prices):
      if prices[left] < prices[right]:
        maxProfit = max(max , prices[right]-prices[left])
      else:
        left = right
      right += 1
    return maxProfit

  if __name__ == "__main__":
    