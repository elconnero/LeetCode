class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        window = set()

        if len(s) < 2: return ""

        for right in range(len(s)):
            window.add(s[right])
        
        bad_letter = None
        for letter in window:
            if letter.swapcase() in window: continue
            else: 
                bad_letter = letter
                break

        if bad_letter is None:
            return s  # whole string is nice, nothing bad found

        bad_index = s.index(bad_letter)
        left_part = self.longestNiceSubstring(s[:bad_index])
        right_part = self.longestNiceSubstring(s[bad_index+1:])

        return left_part if len(left_part) >= len(right_part) else right_part
    
sol = Solution()

test_cases = [
    "YazaAay",   # "aAa"
    "Bb",         # "Bb"
    "c",          # ""
    "dDzeE",      # "dD"
    "abABB",      # "abABB"
    "abA",        # "" (no nice substring exists)
    "aAabCBc",    # "aAabCBc" (whole string is nice)
]

for s in test_cases:
    output = sol.longestNiceSubstring(s)
    print(output, " ", s)