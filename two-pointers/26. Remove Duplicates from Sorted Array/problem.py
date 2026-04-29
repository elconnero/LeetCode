class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left = 0
        right = 1 
        res = 0

        while right < len(nums):
    
            if nums[left] != nums[right]: 
                left += 1
                nums[left] = nums[right]
            right += 1

        return left + 1


nums = [1, 1, 2]
sol = Solution()
print(sol.removeDuplicates(nums))