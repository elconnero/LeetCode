class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        nums1[:] = nums1[:m] + nums2
        nums1.sort()

sol = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = len(nums2)

sol.merge(nums1, m, nums2, n)
print(nums1)
        