class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for i in range(26):
            char = chr(97 + i)
            if char not in sentence:
                return False
        return True
        
        # lst = []
        # for i in sentence:
        #     lst.append(ord(i))
        # for i in range(26):
        #     if i+97 not in lst:
        #         return False
        # return True