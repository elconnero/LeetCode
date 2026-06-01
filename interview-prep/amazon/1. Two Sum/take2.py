class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in seen: return [seen[compliment], i]
            else: seen[num] = i

sol = Solution()

print(sol.twoSum([2,7,11,15], 9))