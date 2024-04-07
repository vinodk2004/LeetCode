class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        char = {')': '(', '}': '{' , ']': '['}
        stack = []
        for i in s:
            if i in ['(', '{' , '[']:
                stack.append(i)
            elif stack and char[i] == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0