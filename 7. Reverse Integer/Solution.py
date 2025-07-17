class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        neg = False
        if x < 0:
            neg = True
            x = abs(x)
        
        rev = ''
        
        for i in range(len(str(x))):
            rem = x % 10
            rev += str(rem)
            x = x // 10
        
        out = int(rev)

        if neg:
            out *= -1
        
        if out < -2**31 or out > 2**31 - 1:
            return 0

        return out
