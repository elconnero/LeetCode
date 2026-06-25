class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        if k == 1: return 0
        
        diff = 0
        nums = sorted(nums)
        for num in range(len(nums)-k):
            window = 0
            for elements in k: window += nums[num+elements]
            diff = min(diff, window)
                


sol = Solution()

test_cases = [
    ([90], 1),              # 0   (only one score, k=1, diff is always 0)
    ([9, 4, 1, 7], 2),      # 2   (pick [7,9] or similar closest pair)
    ([4, 7, 9, 1, 0], 2),   # 1   (pick the two closest scores)
    ([1, 2, 3, 4, 5], 3),   # 2   (pick any 3 consecutive after sorting)
    ([5, 5, 5, 5], 2),      # 0   (all same value)
    ([1, 100], 2),          # 99  (forced to use both, k=2 means all scores)
]

for nums, k in test_cases:
    output = sol.minimumDifference(nums, k)
    print(output, " ", k, " ", nums)