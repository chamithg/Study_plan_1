class Solution:
    def runningSum(self, nums):
        output = []
        sum = 0
        for i in nums:
            sum += i
            output.append(sum)
            
        return(output)
        
        


obj = Solution()
nums = [1,2,3,4]

print(obj.runningSum(nums))