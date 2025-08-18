class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = [i for i in str(num)]
        idx = str(num).find('6')
        temp[idx] = '9'
        num = ''.join(temp)
        return int(num)
