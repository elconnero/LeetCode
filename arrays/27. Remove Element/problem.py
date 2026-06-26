# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
    
#         if len(nums) == 1:
#             if nums[0] == val: return 0
#             else: return len(nums)

#         if len(nums) == 2 and nums[1] == val: nums[:] = nums[:1]
#         if len(nums) == 2 and nums[0] == val: nums[:] = nums[1:] 
#         if len(nums) == 2 and (nums[0] == val and nums[1] == val): 
#             nums[:] = []
            
        
#         left = 0 
#         right = len(nums) - 1
#         found_val = False


#         while left < right:
#             temp = None
#             if nums[right] == val: 
#                 found_val = True
#                 right -= 1
#             if nums[left] == val: 
#                 found_val = True
#                 temp = nums[left]
#                 nums[left] = nums[right]
#                 nums[right] = temp
#                 left += 1
#             else: left += 1
        
#         if found_val == True:
#             nums[:] = nums[:nums.index(val)]
#             return len(nums)
#         else: return len(nums)
    
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1

        return left

sol = Solution()

test_cases = [
    ([3, 2, 2, 3], 3),              # 2  (keep the two 2's)
    ([0, 1, 2, 2, 3, 0, 4, 2], 2),  # 5  (keep 0,1,3,0,4)
    ([1], 1),                        # 0  (only element matches val, nothing left)
    ([1], 2),                        # 1  (val not even in array, keep everything)
    ([4, 4, 4, 4], 4),               # 0  (all elements equal val)
    ([2, 3, 4, 5], 9),               # 4  (val not present, keep all 4)
    ([3,2,2,3], 3),
    ([4,5], 5),
    ([4,5], 4),
    ([2,2,3], 3),
    ([2,3,3], 3),
    ([3,3], 3)

]

for nums, val in test_cases:
    output = sol.removeElement(nums, val)
    print(output, " ", val, " ", nums)