# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
        
#         res = len(nums) - nums.index(max(nums))

#         for num in nums:
#             if num == target:
#                 if len(nums) == 1: return 0
#                 else: return res
#         return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        for num in nums:
            if target == num: return nums.index(target)
        return -1
            


sol = Solution()

test_cases = [
    ([4, 5, 6, 7, 0, 1, 2], 0),  # 4 (index)
    ([4, 5, 6, 7, 0, 1, 2], 3),  # -1 (not found)
    ([1], 0),                     # -1 (not found)
    ([1], 1),                     # 0 (index)
    ([1, 3], 3),                  # 1 (index)
    ([3, 4, 5, 1, 2], 4),        # 1 (index)
    ([3, 4, 5, 1, 2], 6),        # -1 (not found)
]

for arr, target in test_cases:
    output = sol.search(arr, target)
    print(output, " ", target, " ", arr)