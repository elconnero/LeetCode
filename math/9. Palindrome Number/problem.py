class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0: return False
        x = str(x)

        j = len(x) -1
        for i in range(len(x)):
            if x[i] != x[j]: return False
            if (i == j or i+1 == j) and x[i] == x[j]: return True
            j -= 1
        

test = Solution()
testcases = [-121,10,121,1001,100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001]
for i in range(len(testcases)): print(f"{i}. {testcases[i]} =", test.isPalindrome(testcases[i]))

# KEEP FORGETING THIS IS BE BEST WAY :'0
# class Solution(object):
#     def isPalindrome(self, x):
#         s = str(x)
#         if s == s[::-1]:
#             return True   
#         else:
#             return False     