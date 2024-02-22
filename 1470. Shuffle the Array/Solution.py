class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out = []
        if len(nums)%2 != 0:
            return out
        for i in range(n):
            out.extend([nums[i], nums[i+n]])
        return out

