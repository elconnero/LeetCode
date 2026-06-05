class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        seen = {}

        for char in s:
            if char in seen: seen[char]  += 1
            else: seen[char] = 1 

        for char in t:
            if char not in seen: return False
            seen[char] -= 1
            if seen[char] < 0: return False
        return True

sol = Solution()

test_case_s = [
    "anagram",
    "rat",
    "car"
]

test_case_t = [
    "nagaram",
    "car",
    "rac"
]

for i in range(len(test_case_s)): print(sol.isAnagram(test_case_s[i], test_case_t[i]))