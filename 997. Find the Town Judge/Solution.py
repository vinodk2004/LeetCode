class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        town_judge = -1
        if not trust and n == 1:
            return 1
        a = []
        b = []
        for i in trust:
            a.append(i[0])
            b.append(i[1])
        a = set(a)
        for i in range(1,n+1):
            if i not in a and b.count(i) >= n-1:
                town_judge = i
        return town_judge