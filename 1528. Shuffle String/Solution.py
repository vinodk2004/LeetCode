class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        out = [0]*len(s)
        for i, pos in enumerate(indices):
            out[pos] = s[i]
        return ''.join(out)