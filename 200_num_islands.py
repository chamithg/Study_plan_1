class Solution:
    def numIslands(self, grid):
        numIslands =0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]=="1":
                    numIslands +=1
                    if grid[r-1][c] =="1" or grid[r][c-1] =="1":
                        numIslands -=1
                        
        return numIslands


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
obj = Solution()
print(obj.numIslands(grid))