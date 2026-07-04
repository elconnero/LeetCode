class Solution:
    def mySqrt(self, x: int) -> int:
        
        n = x
        y = (n+1)//2
        while y < n:
            n = y
            y = (n + x//n)//2
        return n
