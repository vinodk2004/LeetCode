class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_op = 101
        for i in range(len(blocks)-(k-1)):
            count = blocks[i:i+k].count('W')
            if count < min_op:
                min_op = count
        return min_op
