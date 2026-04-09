# My way, there is an error in math, lets see how neet does it and then we can come back to this.
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        answer = 0

        while left < right:

            answer = max(answer, (right-left)*min(height[left],height[right]))

            if height[left] < height[right]: left += 1
            else: right -= 1
            
        
        return answer

#Neet way
# class Solution(object):
#     def maxArea(self, height):

#         res, left,  right = 0, 0, len(height)-1

#         while left < right:

#             area = (right - left) * min(height[left], height[right])
#             res = max(res, area)

#             if height[left] < height[right]: left += 1
#             else: right -= 1
#         return res




test = Solution()

output = test.maxArea([1,2,4,3])
print(output)