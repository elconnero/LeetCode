class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end = len(nums) 
        left, right = 0,1

        if len(nums) == 1: return nums

        while right < end:
            if nums[left] == 0 and nums[right] != 0:
                nums[left] = nums[right]
                nums[right] = 0
                left += 1
            elif nums[left] != 0: left += 1
            right += 1 
            
            
sol = Solution()

test_cases = [
    [0, 1, 0, 3, 12],   # [1, 3, 12, 0, 0]
    [0],                 # [0]  (single zero)
    [1],                 # [1]  (single non-zero)
    [0, 0, 0, 0],       # [0, 0, 0, 0]  (all zeros)
    [1, 2, 3, 4],       # [1, 2, 3, 4]  (no zeros, unchanged)
    [0, 0, 1],          # [1, 0, 0]
    [1, 0, 0, 0, 2],    # [1, 2, 0, 0, 0]
]

for nums in test_cases:
    sol.moveZeroes(nums)
    print(nums)