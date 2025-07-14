class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            longest = max(longest, len(s[l:r+1]))
        return longest


