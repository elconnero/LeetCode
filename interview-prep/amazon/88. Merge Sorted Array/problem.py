from collections import deque

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        nums1[m:] = nums2
        nums1.sort()
        
sol = Solution()

nums1 = [1,2,3,0,0,0]
print(sol.merge(nums1, 3,[2,5,6], 3))
print(nums1)