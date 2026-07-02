class Solution:
    def lengthOfLastWord(self, s: str) -> int: return len(s.split()[-1])


"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count the last word
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length
"""
#Best way to hangle memory



sol = Solution()

test_cases = [
    "Hello World",          # 5  ("World" has 5 characters)
    "   fly me   to   the moon  ",  # 4  ("moon", ignore trailing spaces)
    "luffy is still joyboy", # 6  ("joyboy")
    "a",                    # 1  (single character)
    "a ",                   # 1  (trailing space, last word is still "a")
    "  a",                  # 1  (leading space, last word is "a")
    "today is a great day",  # 3  ("day")
]

for s in test_cases:
    output = sol.lengthOfLastWord(s)
    print(output, " ", repr(s))