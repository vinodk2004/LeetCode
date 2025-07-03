class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for i in range(len(nums)):
            map[nums[i]] += 1

        sort_map = dict(sorted(map.items(), key = lambda item: item[1], reverse = True))
        
        freq = list(sort_map.keys())
        return freq[0:k]
