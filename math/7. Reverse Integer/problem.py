class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        switch = 1
        if x < 0: switch = -1
        x = abs(x)
        while x != 0:
            digit = x % 10
            x = x // 10
            ans = ans * 10 + digit
        
        if ans < -2**31 or ans > 2**31 - 1: return 0
        else: return ans * switch
        
