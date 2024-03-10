class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mini = nums1 if len(nums1) < len(nums2) else nums2
        maxi = nums1 if len(nums1) > len(nums2) else nums2
        nums1 = []
        for i in mini:
            if i in maxi and i not in nums1:
                nums1.append(i)

        return nums1
