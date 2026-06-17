class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        res = 0
        counter = {}

        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1

            # check if window is valid
            most_frequent = max(counter.values())
            window_size = right - left + 1

            if window_size - most_frequent > k:
                # shrink window
                counter[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res


        


sol = Solution()

test_cases = [
    ("ABAB", 2),    # 4  (replace 2 A's or B's to get "AAAA" or "BBBB")
    ("AABABBA", 1), # 4  (replace 1 character to get "AABBBBA" or similar)
    ("AAAA", 0),    # 4  (already all same character)
    ("ABCD", 1),    # 2  (can only fix 1 character)
    ("A", 0),       # 1  (single character)
    ("AABB", 2),    # 4  (replace 2 to get "AAAA" or "BBBB")
    ("ABBB", 2),    # 4  (replace 2 A's)
]

for s, k in test_cases:
    output = sol.characterReplacement(s, k)
    print(output, " ", k, " ", s)