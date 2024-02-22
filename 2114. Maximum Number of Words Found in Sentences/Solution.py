class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        temp = []
        max = 0
        for i in sentences:
            temp = i.split(' ')
            if max < len(temp):
                max = len(temp)
        return max