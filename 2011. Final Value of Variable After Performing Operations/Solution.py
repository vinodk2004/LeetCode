class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for opr in operations:
            if '+' in opr:
                x += 1

            elif '-' in opr:
                x -= 1
        return x
