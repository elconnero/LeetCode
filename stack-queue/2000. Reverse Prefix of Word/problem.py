class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        stack = []
        word = list(word)
        found = False

        while word:
            letter = word.pop(0)
            stack.append(letter)
            if letter == ch:
                found = True
                break
            
        if found:
            return "".join(reversed(stack)) + "".join(word)
        else:
            return "".join(stack)  # ch not found, return word unchanged
sol = Solution()

test_cases = [
    ("abcdefd", "d"),   # "dcbaefd"  (reverse "abcd" → "dcba")
    ("xyxzxe", "z"),    # "zxyxe"   (reverse "xyz" → wait, "xyxz" → "zxyx")
    ("abcd", "z"),      # "abcd"    (ch not in word, no change)
    ("hello", "l"),     # "leho"    (reverse "hel" → "leh")
    ("a", "a"),         # "a"       (single char equals ch)
    ("aaa", "a"),       # "aaa"     (ch is first char, reverse just "a")
]

for word, ch in test_cases:
    output = sol.reversePrefix(word, ch)
    print(output, " ", ch, " ", word)