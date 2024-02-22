class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # dit = {}
        # for val in nums:
        #     if val not in dit:
        #         dit[val] = 1
        #     else:
        #         dit[val] += 1
        # element = max(dit, key=dit.get)
        # if dit[element] > len(nums) // 2:
        #     return element
        # else:
        #    return None

        nums.sort()
        return nums[len(nums) // 2]
        