class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            n = len(words[i])
            for j in range(i+1,len(words)):
                if words[i] == words[j][:n] and words[i] == words[j][-n:]:
                    count += 1
        return count