# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """

#         if len(s) == 1: return None
#         left, right = 0, len(s) - 1

#         while left < right:

#             temp = s[left]
#             s[left] = s[right]
#             s[right] = temp
#             left += 1
#             right -= 1

#Best time solution:
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
"""

#After seeing this, doing some modifications to my code.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # if len(s) == 1: return None
        left, right = 0, len(s) - 1

        while left < right:

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# This is the best way for memory
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        return s
"""


sol = Solution()

test_cases = [
    ["h", "e", "l", "l", "o"],   # ["o", "l", "l", "e", "h"]
    ["H", "a", "n", "n", "a", "h"],  # ["h", "a", "n", "n", "a", "H"]
    ["a"],                        # ["a"]  (single element, unchanged)
    ["a", "b"],                   # ["b", "a"]  (two elements)
    ["a", "b", "c"],              # ["c", "b", "a"]
    ["z", "z", "z"],              # ["z", "z", "z"]  (all same, unchanged)
]

for s in test_cases:
    sol.reverseString(s)
    print(s)