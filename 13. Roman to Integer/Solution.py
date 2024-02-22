class Solution:
    def romanToInt(self, s: str) -> int:
        table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        prevI = False
        prevX = False
        prevC = False
        for i in s:
            if i == 'I':
                ans += table['I']
                prevI = True

            elif i == 'V':
                ans += table['V']
                if prevI:
                    ans -= 2
                    prevI = False

            elif i == 'X':
                ans += table['X']
                prevX = True
                if prevI:
                    ans -= 2
                    prevI = False

            elif i == 'L':
                ans += table['L']
                if prevX:
                    ans -= 20
                    prevX = False

            elif i == 'C':
                ans += table['C']
                prevC = True
                if prevX:
                    ans -= 20
                    prevX = False
            
            elif i == 'D':
                ans += table['D']
                if prevC:
                    ans -= 200
                    prevC = False
            
            elif i == 'M':
                ans += table['M']
                if prevC:
                    ans -= 200
                    prevC = False
        return ans

            