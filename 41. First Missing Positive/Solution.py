class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # temp = set(nums)
        # n = len(nums)
        # for i in range(1,n+1):
        #     if i not in temp:
        #         return i
        #     else:
        #         temp.remove(i)
        # return n+1

        num = 1
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == num:
                num += 1
        return num 

                