class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        out = '1'
        out += s.count('0') * '0'
        out += (s.count('1') - 1) * '1'
        return out[::-1]