class Solution:
    def reverseVowels(self, s: str) -> str:
        
        if len(s) == 1: return s

        s = list(s)
        left, right = 0, len(s) - 1
        vowels = set('aeiouAEIOU')

        while left < right:

            if (s[left] in vowels) and (s[right] in vowels): 
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] not in vowels: left += 1
            elif s[right] not in vowels: right -= 1
        return "".join(s)
    
# This is super interesting, I really like why they have it this way. 
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and s[left] not in vowels:
                left += 1

            while left < right and s[right] not in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return "".join(s)
"""

#This is the best memory use
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        st=0
        ed=len(s)-1
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        while st<ed:
            if s[st] not in vowels:
                st += 1
            elif s[ed] not in vowels:
                ed -= 1
            else:
                tmp = s[st]
                s = s[:st]+s[ed]+s[st+1:]
                s = s[:ed]+tmp+s[ed+1:]
                st += 1
                ed -= 1
        return s
"""
    
sol = Solution()

test_cases = [
    "IceCreAm",   # "AceCreIm"
    "leetcode",   # "leotcede"
    "a",          # "a"    (single vowel, unchanged)
    "b",          # "b"    (no vowels, unchanged)
    "aA",         # "Aa"   (two vowels, swap)
    "hello",      # "holle"
    "AEIOU",      # "UOIEA"  (all vowels, fully reversed)
    "bcdfg",      # "bcdfg"  (no vowels at all, unchanged)
    "aeiou",      # "uoiea"
]

for example in test_cases:
    output = sol.reverseVowels(example)
    print(output, " ", example)