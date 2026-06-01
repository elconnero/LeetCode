
# class Solution: # Space/Time = O(n)
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen = {}
#         for i, val in enumerate(nums):
#             compliment = target - val
#             if compliment in seen: return[seen[compliment], i]
#             else: seen[val] = i
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)): #t=n
#             for j in range(len(nums)-1,-1,-1): #t=n
#                 if nums[i] + nums[j] == target and i != j: return[i,j] #S=O(n)
# # Time: O(n²) - nested loops
# # Space: O(1) - no extra data structures

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        first = 0
        last = len(nums) -1

        while first < last:

            if nums[first] + nums[last] == target and first != last: return [first, last]
            elif nums[first] + nums[last] < target: first += 1
            elif nums[first] + nums[last] > target: last -= 1


sol = Solution()

print(sol.twoSum([2,7,11,15], 9))