class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val not in ('+', '-', '*', '/'):
                stack.append(int(val))
            else:
                j = stack.pop()
                i = stack.pop()
                if val == '+':
                    stack.append(i + j)
                elif val == '-':
                    stack.append(i - j)
                elif val == '*':
                    stack.append(i * j)
                else:
                    stack.append(int(i/j))
        return int(stack[0])