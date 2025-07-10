class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        d = {}
        out = []

        for i, val in enumerate(temp):
            if val not in d:
                d[val] = i
        
        for num in nums:
            out.append(d[num])

        return out                
