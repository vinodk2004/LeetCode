class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
      j = 0
      lst =""
      for i in range(len(s)):
        flag = True
        while flag:
          if j >= len(t):
            return False
          if s[i] == t[j]:
            print(j)
            lst = lst + s[i]
            flag = False
            j += 1
          else:
            j += 1
      print(lst)
      if lst == s:
        return True




