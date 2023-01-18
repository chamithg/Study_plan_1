class Solution:
    def findAnagrams(self, s: str, p: str):
        
        
        # Solution 1 works but poor time complexity
        # output = []
        # if len(s)<len(p):return output
        # # initiate two pointers
        # start = 0
        # end = len(p)
        # # initiated a map for the search string
        # pMap = {}
        # #  create p map:
        # for i in p:
        #     if i in pMap:
        #         pMap[i] += 1
        #     else:
        #         pMap[i] =1
        # while end <= len(s):
            
        #     # create a temperary counter s[start] in pMap
        #     if s[start] in pMap:
        #         tempMap = {}
        #         for i in range(start,end):
        #             if s[i]in tempMap:
        #                 tempMap[s[i]] +=1
        #             else:
        #                 tempMap[s[i]] =1
        #         if pMap == tempMap: output.append(start)
        #     start +=1
        #     end +=1
        # return output
        
        
        # Solution 2 --> Optimal solution
        output = []
        if len(s)<len(p):return output
        start = 0
        end = len(p)
        pMap = {}
        sMap ={}
        for i in p:
            if i in pMap:
                pMap[i] += 1
            else:
                pMap[i] = 1
                
        for i in range(start,end):
            if s[i] in sMap:
                sMap[s[i]] +=1
            else:
                sMap[s[i]] = 1
        
        while end <= len(s):
            print(pMap, sMap)
            if pMap == sMap: output.append(start)
            #  update old start count
            if sMap[s[start]] == 1: del sMap[s[start]]
            else:sMap[s[start]]-=1
            # update New start 
            start += 1
            # update New end
            end += 1
            # update new endCount 
            if end <= len(s):
                if s[end-1] in sMap:
                    sMap[s[end-1]] += 1
                else:
                    sMap[s[end-1]] = 1
            
            
        return output

# s = "cbaebabacd"
# p = "abc"

s = "abab"
p = "ab"
obj = Solution()
print(obj.findAnagrams(s,p))