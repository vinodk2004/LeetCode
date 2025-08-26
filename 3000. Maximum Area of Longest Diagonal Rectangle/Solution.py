class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diag = []

        for rec in dimensions:
            diag.append( sqrt(rec[0]**2 + rec[1]**2) )
        
        max_val = max(diag)
        idx = [i for i, val in enumerate(diag) if val == max_val]

        area = []
        max_area = -float('inf')

        for i in idx:
            max_area = max(max_area, dimensions[i][0] * dimensions[i][1])
        
        return max_area
