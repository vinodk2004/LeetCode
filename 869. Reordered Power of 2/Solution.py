import itertools

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s_digits = str(n)
        perms = list(itertools.permutations(s_digits))
        for s_num in perms:
            if s_num[0] == '0':
                continue
            num = int(''.join(s_num))
            if (num > 0) and ((num & (num-1)) == 0):
                return True
        return False
