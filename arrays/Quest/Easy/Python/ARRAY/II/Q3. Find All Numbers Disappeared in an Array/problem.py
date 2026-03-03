# My way attempt 1
# class Solution(object):
#     def findDisappearedNumbers(self, nums):
        
#         new_array = list(range(1, len(nums) + 1)) 
#         missing = []

#         for i in new_array:
#             if i not in nums:
#                 missing.append(i)

#         return missing
# Attempt 2

class Solution(object):
    def findDisappearedNumbers(self, nums):
        
        new_array = list(range(1, len(nums) + 1)) 
        missing = []
        set_nums = set(nums)

        for i in new_array:
            if i not in set_nums:
                missing.append(i)

        return missing