class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        ans = 0

        for num in nums:
            num %= k
            for prev in range(k):
                dp[num][prev] = dp[prev][num] + 1
            ans = max(ans, max(dp[num]))
        return ans
