class Solution:
    def decodeString(self, s: str) -> str:
        strStk = ""
        
        for i,v  in enumerate(s):
            if v =="]":
                tempI = len(strStk)-1
                tempStr = ""
                multiply = ""
                
                # iterate backwords until to find out the string part
                while strStk[tempI]!= "[":
                    tempStr = strStk[tempI] +tempStr
                    tempI-=1
                tempI-=1
                
                #  iterate backwords to find the multiplier
                while strStk[tempI].isnumeric():
                    multiply = strStk[tempI] + multiply
                    tempI -=1
                strStk = strStk[:tempI+1]
                for i in range(int(multiply)):
                    strStk += tempStr  
            else:
                strStk += v
                
        return strStk


# s = "3[a]2[bc]"    
s = "3[a2[c]]"    
obj = Solution()
print(obj.decodeString(s))