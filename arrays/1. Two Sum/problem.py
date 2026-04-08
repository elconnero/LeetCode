# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
        
#         for i in range(1, len(nums)):

#             if nums[i] + nums[i-1] == target:
#                 return [i-1,i]
            
#             if i == len(nums):
#                 return 0

#Trial 2
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(len(nums)-1, -1, -1):

                if nums[i] + nums[j] == target and i != j:
                    return[i,j]
        
        return 0
    
#This is the best way I guess.
    # def twoSum(self, nums, target):
    #     num_map = {}  # number -> index
        
    #     for i, num in enumerate(nums):
    #         complement = target - num
            
    #         if complement in num_map:
    #             return [num_map[complement], i]
            
    #         num_map[num] = i

test = Solution()
output = test.twoSum([3,2,3],6)
print(output)
