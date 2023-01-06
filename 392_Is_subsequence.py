class Solution:
    def isSubsequence(self, s ,t):
        if s =="":
            return True
        pointer = 0
        for i in t:
            if i == s[pointer]:
                pointer +=1
            if pointer>= len(s): return True
              
        return False    
s = "ab"
t = "baab"

obj = Solution()
print(obj.isSubsequence(s,t))