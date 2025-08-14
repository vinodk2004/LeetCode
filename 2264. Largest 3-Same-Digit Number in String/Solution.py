class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_int = -1
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                max_int = max(max_int, int(num[i]))
        
        return '' if max_int == -1 else str(max_int)*3
