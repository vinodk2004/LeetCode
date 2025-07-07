class Solution:
    def maxArea(self, height: List[int]) -> int:
        # container = 0
        # for i in range(len(height)):
        #     dist = [0] * len(height)
        #     for j in range(i, len(height)):
        #         dist[i] = j - i
        #         container = max(container, dist[i]*min(height[i], height[j]))
        # return container

        container = 0
        i = 0
        j = len(height)-1
        while i<j:
            container = max(container, (j-i)*min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return container
