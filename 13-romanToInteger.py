class Solution:
    def romanToInt(self, s: str) -> int:
        l = []
        for i in reversed(range(0,len(s))):
            try:
                if s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X"):
                    l.append(-1)
                elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                    l.append(-10)
                elif s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                    l.append(-100)
                elif s[i] == "M":
                    l.append(1000)
                elif s[i] == "D":
                    l.append(500)
                elif s[i] == "C":
                    l.append(100)
                elif s[i] == "L":
                    l.append(50)
                elif s[i] == "X":
                    l.append(10)
                elif s[i] == "V":
                    l.append(5)
                elif s[i] == "I":
                    l.append(1)
            except:
                if s[i] == "M":
                    l.append(1000)
                elif s[i] == "D":
                    l.append(500)
                elif s[i] == "C":
                    l.append(100)
                elif s[i] == "L":
                    l.append(50)
                elif s[i] == "X":
                    l.append(10)
                elif s[i] == "V":
                    l.append(5)
                elif s[i] == "I":
                    l.append(1)
            print(l)
        n = 0
        for i in range(0,len(l)):
            n+=l[i]
            print(n)
        return n

s = "MCMXCIV"
sol = Solution()
print(sol.romanToInt(s))
