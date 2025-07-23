class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        max_points = 0
        high_p = 'ab'
        low_p = 'ba'
        
        if x < y:
            x, y = y, x
            high_p, low_p = low_p, high_p

        stack = []
        for char in s:
            if char == high_p[1] and stack and high_p[0] == stack[-1]:
                stack.pop()
                max_points += x
            else:
                stack.append(char)

        stack1 = []
        for char in stack:
            if char == low_p[1] and stack1 and low_p[0] == stack1[-1]:
                stack1.pop()
                max_points += y
            else:
                stack1.append(char)

        return max_points
