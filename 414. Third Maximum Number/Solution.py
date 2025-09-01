class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
            
        else:
            return sorted(nums, reverse=True)[2]



        # one = two = three = float('-inf')
        # nums = list(set(nums))
        
        # for i in range(len(nums)):
        #     if nums[i] > one:
        #         three = two
        #         two = one
        #         one = nums[i]
            
        #     elif nums[i] > two:
        #         three = two
        #         two = nums[i]

        #     elif nums[i] > three:
        #         three = nums[i]
            
        #     else:
        #         continue
        
        # return three if three != float('-inf') else one
