#Recursive way0
# class Solution:
#     def climbStairs(self, n: int) -> int:
#        if n <= 2: return n
#        return self.climbStairs(n-1) + self.climbStairs(n-2)

class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 1,2
        for __ in range(n):
            a,b = b, a+b