class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')
        count = 0

        for word in words:
            flag = False
            
            for char in brokenLetters:
                if char in word:
                    flag = True
                    break
            
            if not flag:
                count += 1
        
        return count
