class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        opened = ["(", "{", "["]
        closed = [")", "}", "]"]

        for char in s:
            if char in opened:
                stack.append(char)
            elif char in closed:
                if not stack: return False
                if opened.index(stack[-1]) != closed.index(char): return False
                stack.pop()

        return len(stack) == 0
        

        
    
test = Solution()

example = test.isValid("()")
print(example)
            