class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        ascending = True
        decending = True

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                ascending = False
            elif nums[i] < nums[i+1]:
                decending = False
        return ascending or decending