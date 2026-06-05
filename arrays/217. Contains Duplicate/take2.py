class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        left = 0
        right = 1

        if len(nums) == 1: return False

        while right < len(nums):
            
            if nums[left] == nums[right]: return True
            left += 1 
            right += 1
        return False
    
sol = Solution()

array_testcases = [
    [1,2,3,1], # True
    [1,2,3,4], # False
    [1,1,1,3,3,4,3,2,4,2] #True
]

for i in range(len(array_testcases)): print(sol.containsDuplicate(array_testcases[i]))