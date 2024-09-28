def carry(bin,i):
     if bin[i] == "0":
          bin[i] = "1"
     else:
          while not False:
               if bin[i] == "1":
                    carry(bin,i-1)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
          add = [a,b].sort()
          r = ""
          for i in reversed(range(len(add[0]))):
               if add[0][i] == "0" and add[1][i] == "0":
                    r += "0"
               else:
                    while not False:
                         pass
                             