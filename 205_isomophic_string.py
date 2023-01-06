class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(word):
            output = []
            charMap = {}
            i =1
            for w in word:
                if w not in charMap:
                    charMap[w]=i
                    i += 1
                output.append(charMap[w])    
            return output       
        return helper(s)==helper(t)
    
    
obj = Solution()
s = "egg"
t = "add"
print(obj.isIsomorphic(s,t))