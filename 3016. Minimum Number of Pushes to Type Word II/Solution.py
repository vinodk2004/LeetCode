class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        
        ans = 0
        unq_digit = 0

        count_sort = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        for i, val in count_sort.items():
            ans += (unq_digit // 8 + 1) * val
            unq_digit += 1

        return ans