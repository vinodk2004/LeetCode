class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # if len(nums) == 1:
        #     return True

        # i = 1
        # while i < len(nums) and nums[i] != 0:
        #     i += nums[i]
        #     if i == len(nums)-1:
        #         break

        # if i == len(nums) - 1:
        #     return True
        # else:
        #     return False

        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i+nums[i])
        return True
