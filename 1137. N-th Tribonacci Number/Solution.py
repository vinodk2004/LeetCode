class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        ta = 0
        tb = 1
        tc = 1
        for i in range(3, n+1):
            temp = ta + tb + tc
            ta = tb
            tb = tc 
            tc = temp
        return tc