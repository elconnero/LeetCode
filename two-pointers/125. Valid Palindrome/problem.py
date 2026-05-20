#s[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()
        return s[::-1] == s


test = Solution()

answer = test.isPalindrome("0P")
print(answer)

