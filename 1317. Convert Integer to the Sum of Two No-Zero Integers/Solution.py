class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for num in range(1, n):
            a = num
            b = n - a

            if '0' not in str(a) and '0' not in str(b):
                return [a, b]  
