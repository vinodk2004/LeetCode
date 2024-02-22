class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n*(n+1)//2) - sum(nums)
        # for i in range(len(nums)):
        #     if i not in nums:
        #         return i
        # return len(nums)
