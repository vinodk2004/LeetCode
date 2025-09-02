import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
        return min_heap[0]


        # for i in range(len(nums)):
        #     nums[i] = -nums[i]
        
        # heapq.heapify(nums)

        # for _ in range(k-1):
        #     heapq.heappop(nums)

        # return -heapq.heappop(nums)
        
