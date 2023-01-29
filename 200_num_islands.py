class Solution:
    def numIslands(self, grid):
        height = len(grid)
        width = len(grid[0])
        islands = 0
        def mark_land(r,c):
            if r < 0 or r >= height or c <0 or c>= width or grid[r][c] != "1": return
            grid[r][c] ="x"
            mark_land(r+1,c)
            mark_land(r-1,c)
            mark_land(r,c+1)
            mark_land(r,c-1)
            
        for r in range(height):
            for c in range(width):
                if grid[r][c] == "1":
                    mark_land(r,c)
                    islands+=1
            
        return islands


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
obj = Solution()
print(obj.numIslands(grid))