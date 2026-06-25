# class Solution:
#     def countGoodSubstrings(self, s: str) -> int:

#         left, res, count, window = 0, 0, 0, set()
#         if len(s) < 3: return 0

#         for letter in s:

#             if letter in window:
#                 window.remove(s[left])
#                 left += 1
#             window.add(letter)
#             if len(window) == 3: 
#                 res += 1
#                 window.discard(s[left])
#                 left +=1
#             count += 1
#             if count == 3: count -= 1 
#         return res

class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        res = 0

        for right in range(2, len(s)):
            window = s[right-2:right+1]
            if len(set(window)) == 3:
                res += 1

        return res
        

        
sol = Solution()

test_cases = [
    "xyzzaz",     # 1  ("xyz" is the only good substring)
    "aababcabc",  # 4  ("abc","bca","cab","abc" — check each window of size 3)
    "abc",        # 1  (only one window, all distinct)
    "aaa",        # 0  (no window has 3 distinct chars)
    "ab",         # 0  (string too short for a window of size 3)
    "abcabc",     # 4  (every window of size 3 has distinct chars)
    "wbwqjjyqrcbmfzvqjmlg" #
]

for s in test_cases:
    output = sol.countGoodSubstrings(s)
    print(output, " ", s)








# for letter in range(len(s)):

#             if letter in window:
#                 window.remove(s[letter])
#                 left += 1
#             window.add(s[letter])
#             if len(window) == 3: 
#                 res += 1
#                 window.remove(s[left])
#                 left +=1
#             count += 1
#             if count == 3: count -= 1 
#         return res