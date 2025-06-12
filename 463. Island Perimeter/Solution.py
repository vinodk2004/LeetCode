class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                
                else:
                    perimeter += 4
                    if i and grid[i-1][j] == 1:
                            perimeter -= 2
                    
                    if j and grid[i][j-1] == 1:
                            perimeter -= 2

        return perimeter 
