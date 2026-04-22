# My way
# class Solution(object):
#     def largestRectangleArea(self, heights):
#         """
#         :type heights: List[int]
#         :rtype: int
#         """
#         ans = []

        
#         if len(heights) == 1: return heights[0]

#         # 0 1 2 3 4 5 6 7 8 9
#         #                 i j
#         j = 1
#         sol = 0
#         for i in range(len(heights)):
#             if j >= len(heights): break
#             if heights[i] == 0:  sol = max(sol,heights[j])
#             if heights[j] == 0:  sol = max(sol,heights[i])
#             if heights[i] + heights[j] > sol: 
#                 sol = max(sol, min(heights[i],heights[j])*2)
#             j += 1
                      
#         return sol

#Right way
class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []  # stores indices
        sol = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                sol = max(sol, height * (i - idx))
                start = idx
            stack.append((start, h))

        for idx, height in stack:
            sol = max(sol, height * (len(heights) - idx))

        return sol


#The best way  
# class Solution(object):
#     def largestRectangleArea(self, heights):
#         """
#         :type heights: List[int]
#         :rtype: int
#         """
#         lis=[-1]

#         themax=0
#         heights.append(-1)
#         for i in range(len(heights)):
#             if heights[i]!=heights[i-1]:
#                 lis.append(i-1)
#                 while heights[i]<heights[lis[-1]]:
#                     pop=lis.pop()
#                     if (i-lis[-1]-1)*heights[pop]>themax:
#                         themax=(i-lis[-1]-1)*heights[pop]
                    

#         return themax

test = Solution()
val = [[2,4,6],[2,1,5,6,2,3],[0,9],[9,0],[2,0,2],[2,1,2], ]
for i in range(len(val)): print(test.largestRectangleArea(val[i]))
