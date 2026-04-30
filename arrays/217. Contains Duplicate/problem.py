class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums = sorted(nums)
        left = 0
        right = 1

        if len(nums) == 1: return False

        while right < len(nums):

            if nums[left] == nums[right]: return True
            left += 1
            right += 1
        return False
    
nums = [1,2,4]
sol = Solution()
print(sol.containsDuplicate(nums)) 