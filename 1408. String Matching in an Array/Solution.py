class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        out = []
        for i in range(n):
            for word in words[0:i] + words[i+1:n]:
                if (words[i] in word) and (words[i] not in out):
                    out.append(words[i])
        return out