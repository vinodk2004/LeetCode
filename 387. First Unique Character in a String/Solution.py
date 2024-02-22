class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
            
        for i in range(len(s)):
            if s[i] not in str(s[:i] + s[i+1:]):
                return i
        return -1

        # for i in range(len(s)):
        #     if s.count(s[i]) <= 1:
        #         return i
        # return -1