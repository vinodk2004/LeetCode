class Solution:
    def reverseWords(self, s: str) -> str:
        list_s = s.split()
        return " ".join(list_s[::-1])
