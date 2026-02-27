#Time & Soace Complexity: O(n) | O(n)
class Solution(object):
    def getConcatenation(self, nums):

        if (len(nums) < 1) or (len(nums) > 1000):
            return
        else:
            #From index 0 to wheverever this ends lets make a copy. 
            return nums[:] + nums[:]
    

# check = Solution()

# nums = [0,1,2]
# checkMe = check.getConcatenation(nums)
# print(checkMe)