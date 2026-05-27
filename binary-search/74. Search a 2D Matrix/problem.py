class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left, top = 0,0
        right, bottom = len(matrix) - 1, len(matrix) - 1