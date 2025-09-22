from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())

        count = 0
        for val, fre in freq.items():
            if fre == max_freq:
                count += fre
        
        return count
