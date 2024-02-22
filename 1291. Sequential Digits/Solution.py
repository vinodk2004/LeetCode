class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        a = []

        for i in range(1,10):
            num = i
            next_num = i+1

            while num <= high and next_num <= 9:
                num = num * 10 + next_num
                if low <= num <= high:
                    a.append(num)
                next_num += 1
        a.sort()
        return a

        # digits = "123456789"
        # res=[]
        # n =10

        # # length of the sliding window
        # for length in range( len(str(low)), len(str(high))+1):
        #     # for sliding the window
        #     for start in range(n - length ): 
        #         num = int(digits[start : start + length])
        #         if low <= num <= high:
        #             res.append(num)
        
        # return res
