class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # num = 0
        # i = 0
        # while i < len(nums):
        #     count = 0
        #     while i < len(nums) and nums[i] == 0:
        #         count += 1
        #         i += 1
            
        #     if count > 0:
        #         num += (count * (count+1)) // 2
        #     else: 
        #         i += 1
            
        # return num

        res = 0
        count = 0

        for num in nums:
            if num == 0:
                count += 1
                res += count
            else:
                count = 0

        return res
