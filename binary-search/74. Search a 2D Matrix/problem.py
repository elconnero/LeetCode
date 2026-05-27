# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
#         left, top = 0,0
#         right, bottom = len(matrix[0]) - 1, len(matrix) - 1

#         while top <= bottom and left <= right:
#             col_mid = (left+right)//2
#             row_mid = (top+bottom)//2

#             if matrix[left][row_mid] <= target and matrix[right][row_mid] >= target:

#                 if matrix[row_mid] == target: return True
#                 elif matrix[row_mid] < target: left = row_mid + 1
#                 else: right = row_mid - 1
#             elif matrix[left][row_mid] <= target: top = col_mid + 1
#             elif matrix[right][row_mid] >= target: bottom = col_mid - 1
#         return False
    
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left, top = 0, 0
        right, bottom = len(matrix[0]) - 1, len(matrix) - 1

        while top <= bottom:
            row_mid = (top + bottom) // 2

            if matrix[row_mid][0] <= target and matrix[row_mid][right] >= target:
                while left <= right:
                    col_mid = (left + right) // 2
                    if matrix[row_mid][col_mid] == target: return True
                    elif matrix[row_mid][col_mid] < target: left = col_mid + 1
                    else: right = col_mid - 1
                return False
            elif matrix[row_mid][0] > target: bottom = row_mid - 1
            else: top = row_mid + 1

        return False
                

testcases_arr = [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], [[1,3,5,7],[10,11,16,20],[23,30,34,60]]]
testcases_target = [3,13]

practice = Solution()

for i in range(len(testcases_arr)):
    print(practice.searchMatrix(testcases_arr[i], testcases_target[i]))