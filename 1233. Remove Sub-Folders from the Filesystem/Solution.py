class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # folder.sort()
        # visited = []
        # for val in folder:
        #     visited.append(val)
        #     for i in range(len(val)):
        #         if val[i] == '/' and val[:i] in visited:
        #             visited.pop()
        #             break
        # return visited

        folder.sort()
        visited = [folder[0]]

        for i in range(1, len(folder)):
            prev_dir = visited[-1] + '/'

            if not folder[i].startswith(prev_dir):
                visited.append(folder[i])
        return visited
