class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        out = ''
        for i in s:
            out += i[::-1] + ' '
        return out[:-1]