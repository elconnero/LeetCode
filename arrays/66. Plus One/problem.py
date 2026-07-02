class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        ans = 0
        for i, digit in enumerate(digits):
             cell = digit * (10 ** (len(digits) - 1 - i))
             ans += cell
        ans = ans + 1
        res = []
        for i in range(len(str(ans))): 
            element = str(ans)[i]
            res.append(int(element))
        return res
    
# This is the best way for runtime:
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        for i in range(n-1,-1,-1):
            if digits[i]!=9:
                digits[i]+=1
                return digits
            digits[i]=0
        digits.insert(0,1)
        return digits

"""

sol = Solution()

test_cases = [
    [1, 2, 3],          # [1, 2, 4]  (simple case, just add 1 to last digit)
    [4, 3, 2, 1],       # [4, 3, 2, 2]
    [9],                # [1, 0]     (carry over, single digit 9)
    [9, 9, 9],          # [1, 0, 0, 0] (all 9s, carry all the way through)
    [1, 9, 9],          # [2, 0, 0]  (carry partway through)
    [0],                # [1]        (single zero)
    [9, 9],             # [1, 0, 0]  (two 9s)
    [1, 0, 0, 0],       # [1, 0, 0, 1] (zeros in the middle)
]

for digits in test_cases:
    output = sol.plusOne(digits)
    print(output, " ", digits)