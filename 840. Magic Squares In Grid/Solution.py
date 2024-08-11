class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0

        if len(grid) < 2 or len(grid[0]) < 2:
            return 0

        for i in range(len(grid)-2):
            for j in range(len(grid[i])-2):
                if self.magic_sq(i, j , grid):
                    ans += 1
        
        return ans

    def magic_sq(self, x, y , grid):
        visited = [0] * 10
        for i in range(3):
            for j in range(3):
                num = grid[x+i][y+j]
                if num<1 or num>9 :
                    return False
                if visited[num]:
                    return False
                visited[num] = True
        
        rows, cols = [], []

        for i in range(3):
            row, col= 0, 0 
            for j in range(3):
                row += grid[x+i][y+j]
                col += grid[x+j][y+i]
            rows.append(row)
            cols.append(col)
        
        if rows[0] != rows[1] != rows[2]:
            return False

        if cols[0] != cols[1] != cols[2]:
            return False

        d1 = 0
        for i in range(3):
            d1 += grid[x + i][y + i]

        d2 = 0
        for i in range(3):
            d2 += grid[x + i][y + (2 - i)]


        if d1 != d2:
            return False
        return True
        
            

