class Solution:
    def pivotIndex(self, nums):
        #  solution 1
        # this solution works but time complexity is not good
        
        # for (i,v)- in enumerate(nums):
        #     left =0
        #     right = 0
        #     for l in range(i):
        #         left += nums[l]
        #     for r in range(i+1, len(nums)):
        #         right += nums[r]
        #     if right == left:
        #         return i
                
        # return -1   
        
        # solution 2 --> optimal
        rightSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
            leftSum+= nums[i]
            
        return -1
        
obj = Solution()
nums = [2,1,-1]
nums1 = [1,7,3,6,5,6]
nums2 = [1,2,3]

print(obj.pivotIndex(nums1))