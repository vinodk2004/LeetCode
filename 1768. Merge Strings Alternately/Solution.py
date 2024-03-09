class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ''
        i = 0
        while i < len(word1) or i < len(word2):
            a = word1[i] if i < len(word1) else ""
            b = word2[i] if i < len(word2) else ""
            out += a + b
            i += 1
        return out