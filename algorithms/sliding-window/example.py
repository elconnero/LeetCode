def length_of_longest_substring(s: str) -> int:
    seen = {}  # char -> last seen index
    left = 0
    max_len = 0

    for right, c in enumerate(s):
        if c in seen and seen[c] >= left:
            left = seen[c] + 1  # shrink window past duplicate
        seen[c] = right
        max_len = max(max_len, right - left + 1)

    return max_len


# Examples
print(length_of_longest_substring("abcabcbb"))  # 3 → "abc"
print(length_of_longest_substring("bbbbb"))     # 1 → "b"
print(length_of_longest_substring("pwwkew"))    # 3 → "wke"
print(length_of_longest_substring("dvdf"))      # 3 → "vdf"