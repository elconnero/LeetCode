class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        answer, left, right = 0, 0, len(height) - 1 

        while left < right:
            answer = max(answer, ((right-left)*min(height[left], height[right])))
            if height[left] < height[right]: left += 1
            else: right -= 1
        return answer
    
sol = Solution()

test_cases = [
    [1, 8, 6, 2, 5, 4, 8, 3, 7],   # 49  (lines at index 1 and 8: min(8,7)*7=49)
    [1, 1],                          # 1   (only two lines, min(1,1)*1=1)
    [4, 3, 2, 1, 4],                 # 16  (lines at index 0 and 4: min(4,4)*4=16)
    [1, 2, 1],                       # 2   (lines at index 0 and 2: min(1,1)*2=2)
    [1, 2, 4, 3],                    # 4   (lines at index 1 and 3: min(2,3)*2=4)
    [2, 3, 4, 5, 18, 17, 6],         # 17  (lines at index 4 and 5: min(18,17)*1=17)
]

for height in test_cases:
    output = sol.maxArea(height)
    print(output, " ", height)