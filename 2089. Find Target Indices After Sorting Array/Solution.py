class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        out = []
        for i in range(len(nums)):
            if nums[i] == target:
                out.append(i)
        return out