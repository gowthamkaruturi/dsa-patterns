class Soluton():
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
      result_days=[0]*len(temperatures)
      stk =[]
      for index, temperature in enumerate(temperatures):
        #peek the element in the stack to check if it is not empty and check if it is less than current temperature
        # pop the elemt in the stack until the condtion is valid 
        # 
        while stk and temperatures[stk[-1]] < temperature:
            j = stk.pop()
            result_days[j]= index-j
        stk.append(index)
      return result_days
    def isValid(self, s: str) -> bool:
      stack = []
      for letter in s:
          if letter ==  '{' or letter == '[' or letter== '(':
              stack.append(letter)
          elif len(stack) > 0: 
              if letter =='}' :
                  if stack.pop != '{':
                      return False
              elif letter == ')':
                  if stack.pop != '(':
                      return False
              elif letter == "]":
                  if stack.pop != '[':
                      return False 
          else :
              return False             
      if len(stack) ==0:
          return True
      return False   
    
class Gowtham():
  def __init__(self):
    self.name ="gowtham"

  def getName(self):
    print(self.name)
  
  def setName(self):
    print(self.name)
    
  def hello():
    print("hello")


if __name__ == "__main__":
  g = Gowtham()
  g.getName()
  g.hello()
