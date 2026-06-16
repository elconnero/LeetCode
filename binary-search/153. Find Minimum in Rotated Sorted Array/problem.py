class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
        
        


sol = Solution()

test_cases = [
    [3, 4, 5, 1, 2],
    [4, 5, 6, 7, 0, 1, 2],
    [1],
    [2, 1],
    [2, 3, 4, 5, 1],
]

for arr in test_cases:
    output = sol.findMin(arr)
    print(output, " ", arr)