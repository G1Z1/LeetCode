class Solution:
    def isValid(self, s: str) -> bool:
          openCount = 0
          closeCount = 0
          stack = []
          for c in s:
               print(c)
               try:
                    if (c == "(" or c == "[" or c == "{"):
                         print("Adding opener")
                         stack.append(c)
                         openCount += 1
                         #print(openCount,closeCount)
                         #print(stack)
                    elif (c == ")" or c == "]" or c == "}") and len(stack)==0:
                         print("Missing opener")
                         closeCount += 100
                         #print(openCount,closeCount)
                         break
                    elif c == ")" and stack[-1] == "(":
                         print("() detected, ok")
                         closeCount += 1
                         del stack[-1]
                         #print(openCount,closeCount)
                    elif c == "]" and stack[-1] == "[":
                         print("[] detected, ok")
                         closeCount += 1
                         del stack[-1]
                         #print(openCount,closeCount)
                    elif c == "}" and stack[-1] == "{":
                         print("{} detected, ok")
                         closeCount += 1
                         del stack[-1]
                         #print(openCount,closeCount)
                    else:
                         print("Error = False")
                         closeCount += 100
                         break
               except:
                    break
                    #print(openCount,closeCount)     
          return openCount == closeCount

s = "([)]"
s = "["
s = "]"
s = "){"
s = "(])"
s ="()"
s = "([])"
sol = Solution()
print(sol.isValid(s))


"""
     openCount = 0
     closeCount = 0
     stack = []
     for c in s:
          try:
               if (c == ")" or c == "]" or c == "}") and len(stack)==0:
                    closeCount += 1
                    openCount += -100
               elif c == "(" or c == "[" or c == "{":
                    stack.append(c)
                    openCount += 1
                    print(openCount,closeCount)
               elif c == ")" and stack[-1] == '(':
                    stack.pop(-1)
                    closeCount += 1
                    print(openCount,closeCount)
               elif c == "]" and stack[-1] == '[':
                    stack.pop(-1)
                    closeCount += 1
                    print(openCount,closeCount)
               elif c == "}" and stack[-1] == '{':
                    stack.pop(-1)
                    closeCount += 1
                    print(openCount,closeCount)

               else:
                    pass
                    print(openCount,closeCount)
          except:
               pass
               print(openCount,closeCount)
     print(stack)

     return openCount == closeCount
"""