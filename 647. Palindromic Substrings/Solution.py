class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        for i in range(2, len(s) + 1):
            for j in range(0, len(s) - i + 1):
                val = s[j : j + i]
                if val == val[::-1]:
                    count += 1
        return count
