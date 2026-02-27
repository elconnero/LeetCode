#Trial one, to be fiar, I feel as the instructions assumed this was sorted that is what the examples looked like. 
# class Solution(object):
#     def findErrorNums(self, nums):
#         for i in range(len(nums)):
#             error_array = []
#             if nums[i] <= nums[len(nums)-1]:
#                 if nums[i] == nums[i+1]:
#                     error_array.append(nums[i])
#                     error_array.append(nums[i]+1)
#                     return error_array
#                 else:
#                     continue
#             else:
#                 return

class Solution(object):
    def findErrorNums(self, nums):

        accounting_array = []
        if not nums: return []

        dup = None

        # find the duplicate
        for i in range(len(nums)):
            if nums[i] in accounting_array:
                if dup is None:   # only record it once
                    dup = nums[i]
            else:
                accounting_array.append(nums[i])

        # find the missing number (1..n)
        missing = None
        n = len(nums)
        for val in range(1, n + 1):
            if val not in accounting_array:
                missing = val
                break

        return [dup, missing]

                

            

                
                
        
nums = [2,2]    
workit = Solution()
we_working = workit.findErrorNums(nums)

print(we_working)