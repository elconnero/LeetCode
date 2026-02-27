# My attempt without doing any research:

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        
        if not nums:
            return
        
        new_array = [None] * len(nums)

        for i in range(len(nums)):
            increment = 0
            val = nums[i]
            for count in nums:
                if count < val:
                    increment += 1
            new_array[i] = increment
