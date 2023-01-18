class Solution:
    def minCostClimbingStairs(self, cost):
        steps = len(cost)
        costCounter = [0]*steps
        for i in range(steps):
            if i == 0 or i ==1 : costCounter[i]= cost[i]
            else: costCounter[i]= min(cost[i]+ costCounter[i-1], cost[i] + costCounter[i-2])
        print(costCounter)    
        return min(costCounter[-1],costCounter[-2])   
            


cost = [1,100,1,1,1,100,1,1,100,1]            
obj= Solution()
print(obj.minCostClimbingStairs(cost))
           
