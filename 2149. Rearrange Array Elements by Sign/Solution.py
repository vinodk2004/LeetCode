class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_int, neg_int = [], []
        n = len(nums)
        for i in nums:
            if i >= 0:
                pos_int.append(i)
            else:
                neg_int.append(i)
        nums = []
        for i in range(n//2):
            nums.append(pos_int[i])
            nums.append(neg_int[i])
        return nums