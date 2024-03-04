class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        return word[:i+1][::-1] + word[i+1:]

        # if ch not in word:
        #     return word
        # for i in range(len(word)):
        #     if word[i] == ch:
        #         out = word[0:i+1][::-1] + word[i+1:]
        #         break
        # return out

