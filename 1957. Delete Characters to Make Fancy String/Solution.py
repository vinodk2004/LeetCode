class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s

        unique_s = ''
        for i in range(len(s)-2):
            if not (s[i] == s[i+1] and s[i] == s[i+2]):
                unique_s += s[i]
        return unique_s + s[-2] + s[-1]
