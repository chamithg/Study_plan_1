class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def remove_backSpace(string):
            out =""
            for i in string:
                if i =="#":
                    if len(out)>0:out = out[:-1]
                else:
                    out += i
            return out
        
        return remove_backSpace(s) == remove_backSpace(t)


s = "ab#c"
t = "ad#e"

obj = Solution()
print(obj.backspaceCompare(s,t))