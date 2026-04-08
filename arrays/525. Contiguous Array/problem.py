# Trial 1
# class Solution(object):
#     def findMaxLength(self, nums):


#         count_1, count_0, ans = 0, 0, 0
#         arr1, arr0 = [0], [0]
#         for i in range(1, len(nums)):
            
#             print(f"{i}. nums[i] ={nums[i]}")
#             if nums[i] == nums[i-1]:

                
#                 if nums[i] == 1: 
#                     print(i, ".  Adding a 1 to 1")
#                     count_1 += 1
#                 else: 
#                     print(i, ".  Adding a 1 to 0")
#                     count_0 += 1
#             elif nums[i] != nums[i-1]:

#                 arr1.append(count_1)
#                 arr0.append(count_0)
#                 print(f"Count 1 = {count_1}, Count 2 = {count_0}")
#                 count_1, count_0 = 0, 0

#         ans = max(arr1) + max(arr0)
#         print(f"Answer = {ans}")
#         return ans 

class Solution(object):
    def findMaxLength(self, nums):
        
        nums = [1 if x == 1 else -1 for x in nums]
        pre_arr = [0]
        
        for num in nums:
            pre_arr.append(pre_arr[-1] + num)

        d = {0: 0}
        ans = 0
        for i in range(1, len(pre_arr)):
            if pre_arr[i] in d:
                ans = max(ans, i - d[pre_arr[i]])
            else:
                d[pre_arr[i]] = i
        
        return ans
        
        
        

                


test = Solution()
arr = [0,1,1,1,1,1,0,0,0]
output = test.findMaxLength(arr)
print(output, " ",  len(arr), arr)
