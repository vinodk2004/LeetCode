class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = 0
        curr_sum = 0
        l = 0
        visited = set()

        for r in range(len(nums)):
            while nums[r] in visited:
                curr_sum -= nums[l]
                visited.remove(nums[l])
                l += 1
            
            visited.add(nums[r])
            curr_sum += nums[r]
            max_score = max(max_score, curr_sum)
        
        return max_score
