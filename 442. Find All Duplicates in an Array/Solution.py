class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        out = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                out.append(abs(i))
            nums[abs(i)-1] = -1 * nums[abs(i)-1]
        return out