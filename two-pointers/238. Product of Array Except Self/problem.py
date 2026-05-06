
# O(n^(1/2)) time
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         res = [0] * len(nums)

#         for i in range(len(nums)):
#             ans = 1
#             for j in range(len(nums)):

#                 if i == j:
#                     continue
#                 else:
#                     ans *= nums[j]
#             res[i] = ans
            

#         return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # prefix pass
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        # suffix pass
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
    
test = Solution()
testcase_nums = [[1,2,3,4], [-1,1,0,-3,3], [1,2]]
for i in range(len(testcase_nums)):
    prints = test.productExceptSelf(testcase_nums[i])
    print(prints)
