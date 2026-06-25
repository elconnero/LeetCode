# Missed the mark
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
#         left = 0
#         for right in range(len(nums)):
#             if (right - left == k+1) and (left < right): left += 1
#             if (right - left <= k) and (nums[left] == nums[right]) and (abs(right - left) <= k) and (left != right): return True
            
#         return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                window.remove(nums[left])
                left += 1

            if nums[right] in window:
                return True

            window.add(nums[right])

        return False
    
sol = Solution()

test_cases = [
    ([1, 2, 3, 1], 3),        # True   (two 1's, gap=3, k=3)
    ([1, 0, 1, 1], 1),        # True   (two 1's at indices 2,3, gap=1, k=1)
    ([1, 2, 3, 1, 2, 3], 2),  # False  (gaps all too big)
    ([1, 2, 3, 1, 2, 3], 3),  # True   (gap=3, k=3, now allowed)
    ([1], 1),                 # False  (only one element, no pair)
    ([1, 1], 1),               # True   (adjacent duplicates, gap=1)
    ([99, 99], 0),             # False  (k=0 means gap must be 0, impossible for distinct indices)
    ([0,1,2,3,2,5], 3),           #True
]

for nums, k in test_cases:
    output = sol.containsNearbyDuplicate(nums, k)
    print(output, " ", k, " ", nums)