class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        v, c = 0, 0
        vowels = set('aeiouAEIOU')
        for char in word:
            if not char.isalnum():
                return False
            
            if char.isalpha():
                if char in vowels:
                    v += 1
                else:
                    c += 1
        return True if v>0 and c>0 else False
