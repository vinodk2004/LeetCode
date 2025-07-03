class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # left, right = [1] * n, [1] * n

        # for i in range(1, n):
        #     left[i] = left[i-1] * nums[i-1]
        
        # for i in range(n-1, 0, -1):
        #     right[i-1] = right[i] * nums[i]
        
        # for i in range(len(nums)):
        #     left[i] = left[i] * right[i]

        # return left

        n = len(nums)
        left_prod = 1
        prod = [1] * n

        for i in range(n):
            prod[i] *= left_prod
            left_prod *= nums[i]

        right_prod = 1

        for i in range(n-1, -1, -1):
            prod[i] *= right_prod
            right_prod *= nums[i]
        
        return prod
