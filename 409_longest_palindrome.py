class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        numMap = {}
        odd_found = False
        total_length = 0
        # create counter object
        for i in s:
            if i in numMap:
                numMap[i]+=1
            else:
                numMap[i] =1
        print(numMap)
        for key, value in numMap.items():
            if value % 2 == 0:
                total_length += value
            elif odd_found:
                if value>1:
                    total_length += value -1
            else:
                odd_found = True
                total_length += value
                    
        return total_length          
            
        
s ="civilwartestingwhetherthatnaptionoranynar"      
obj = Solution()
print(obj.longestPalindrome(s))