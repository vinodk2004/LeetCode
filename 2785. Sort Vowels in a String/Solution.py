class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        t = ''
        v_str = []
        for char in s:
            if char in vowels:
                v_str.append(ord(char))
        
        v_str.sort()
        k = 0

        for char in s:
            if char not in vowels:
                t += char
            else:
                t += chr(v_str[k])
                k += 1
            
        return t
