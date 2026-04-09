# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         i = 0
#         #j = 1
#         k = len(nums) - 1
#         ans = []

#         while i < k:

#             for j in range (0, k+1):
#                 if (nums[i] + nums[j] + nums[k] == 0) and i != j and i != k and j !=k:
#                     if [nums[i], nums[j], nums[k]] not in ans:
#                         ans.append([nums[i], nums[j], nums[k]])
                    
#             i +=1
#             k -=1
#         return ans

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []

        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    if [nums[i], nums[j], nums[k]] not in ans:
                        ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
        return ans


test = Solution()
output = test.threeSum([-1,0,1,2,-1,-4])
print(output)