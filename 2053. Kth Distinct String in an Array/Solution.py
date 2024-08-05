class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        
        distinct = [s for s in arr if count[s] == 1]

        if k <= len(distinct):
            return distinct[k-1]
        return ''