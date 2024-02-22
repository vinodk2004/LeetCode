class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # for val in nums:
        #     while nums.count(val) > 1:
        #         nums.remove(val)
        # return len(nums)
        nums[:] =  sorted(list(set(nums)), key=nums.index)
        return len(nums)
