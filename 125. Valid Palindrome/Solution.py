class Solution:
    def isPalindrome(self, s: str) -> bool:
        out = ''
        for i in s.lower():
            if i.isalnum():
                out += i
        return out == out[::-1]