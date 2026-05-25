class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        s_stack = []
        t_stack = []
        
        for char in s:
            if char.isalpha():
                s_stack.append(char)
            if char == "#" and s_stack: s_stack.pop()

        for char in t:
            if char.isalpha():
                t_stack.append(char)
            if char == "#" and t_stack: t_stack.pop()

        return s_stack == t_stack

        
sol = Solution()
print(sol.backspaceCompare("ab#c", "ad#c"))   # expected True
print(sol.backspaceCompare("ab##", "c#d#"))   # expected True
print(sol.backspaceCompare("a#c", "b"))        # expected False
print(sol.backspaceCompare("a##c", "#a#c"))   # expected True