class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n = len(nums)
        arr = []
        for i in range(n):
            arr.append(nums[i])
            x = nums[i]
            for j in range(i+1, n):
                x += nums[j]
                arr.append(x)

        arr.sort()
        return sum(arr[left-1:right]) % (10**9 + 7)