class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for word in strs:
            map = [0] * 26
            for char in word:
                map[ord(char) - ord('a')] += 1

            dict[tuple(map)].append(word)

        return list(dict.values())
        
