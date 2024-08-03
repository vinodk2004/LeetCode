class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        e_count = [0] * 1001
        count = 0

        for t, a in zip(target, arr):
            if e_count[t] == 0:
                count += 1
            e_count[t] += 1

            if e_count[a] == 1:
                count -= 1
            e_count[a] -= 1

        return count == 0
