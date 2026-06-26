class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target in nums: return nums.index(target)
        if target > max(nums): return len(nums) 
        if target < min(nums): return 0
        else:
            left, right = 0, len(nums) - 1

            while left <= right:

                midpoint = (left + right) // 2

                if target > nums[midpoint]: left = midpoint + 1
                if target < nums[midpoint]: right = midpoint - 1
            return left
        
sol = Solution()

test_cases = [
    ([1, 3, 5, 6], 2),    # 1  (found exactly, at index 2)
    ([1, 3, 5, 6], 2),    # 1  (not found, would insert between 1 and 3)
    ([1, 3, 5, 6], 7),    # 4  (not found, goes past the end)
    ([1, 3, 5, 6], 0),    # 0  (not found, goes before the start)
    ([1], 0),              # 0  (single element, target smaller)
    ([1], 1),              # 0  (single element, target matches)
    ([1], 2),              # 1  (single element, target larger)
    ([-5, -2, 0, 3, 7], -3), # 1 (negative numbers involved)
]

for nums, target in test_cases:
    output = sol.searchInsert(nums, target)
    print(output, " ", target, " ", nums)