class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        visit = set()

        while n not in visit:

            visit.add(n)
            n = self.sOS(n)

            if n == 1: return True
        return False
    
    def sOS(self, n):
        output = 0

        while n != 0:

            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output
    
test = Solution()
output = test.isHappy(14)
print(output)