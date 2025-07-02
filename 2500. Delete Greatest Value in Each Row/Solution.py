class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # sum = 0
        # for i in range(len(grid[0])):
        #     max_row = [0] * len(grid)

        #     for j in range(len(grid)):
        #         max_row[j] = max(grid[j])
        #         grid[j].remove(max_row[j])

        #     sum += max(max_row)
        # return sum

        sum = 0
        for row in grid:
            row.sort()

        for i in range(len(grid[0])):
            sum += max(grid[j][i] for j in range(len(grid)))

        return sum
        
