class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle not in haystack:return -1
        else: return haystack.index(needle)


sol = Solution()

test_cases = [
    ("sadbutsad", "sad"),   # 0   (first "sad" starts right at index 0)
    ("leetcode", "leeto"),  # -1  (not found)
    ("hello", "ll"),        # 2   (starts at index 2)
    ("a", "a"),              # 0   (haystack equals needle)
    ("a", "b"),              # -1  (not found, single chars)
    ("mississippi", "issip"), # 4   (starts at index 4)
    ("abc", ""),              # 0   (empty needle, by convention returns 0)
]

for haystack, needle in test_cases:
    output = sol.strStr(haystack, needle)
    print(output, " ", needle, " ", haystack)