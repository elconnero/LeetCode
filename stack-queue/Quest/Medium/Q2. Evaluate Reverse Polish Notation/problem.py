from collections import deque

class Solution(object):
    def evalRPN(self, tokens):
        
        prac = [None,None,None]
        val = prac[0]
        while tokens:

            if isinstance(val, int):
                if prac[0] is None:
                    prac[0] = val
                if prac[1] is None:
                    prac[1] = val
                val = tokens.popleft()
            elif val == "+":
                print(prac[0])
                print(prac[1])
                result = prac[0] + prac[1]
                val = tokens.popleft()


        return result
    
check = Solution()

tokens = [2,3,"+"]
tokens = deque(tokens)

ans = check.evalRPN(tokens)
print(ans)

            