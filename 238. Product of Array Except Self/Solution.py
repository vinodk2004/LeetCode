class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [1]*n, [1]*n
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]

        for i in range(n-1, 0, -1):
            right[i-1] = right[i] * nums[i]

        for i in range(len(nums)):
            left[i] *= right[i]
            
        return left
        