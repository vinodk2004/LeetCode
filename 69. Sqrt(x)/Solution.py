class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return x
        i = 0
        while True:
            if x == i * i:
                return i
            if x < i * i:
                return i-1
            i += 1