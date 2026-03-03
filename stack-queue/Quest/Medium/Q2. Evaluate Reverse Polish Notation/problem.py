from collections import deque

# My way no research, this one kinda TOUGH

# class Solution(object):
#     def evalRPN(self, tokens):
        
#         prac = [None,None,None]
#         val = prac[0]
#         while tokens:

#             if isinstance(val, int):
#                 if prac[0] is None:
#                     prac[0] = val
#                 if prac[1] is None:
#                     prac[1] = val
#                 val = tokens.popleft()
#             elif val == "+":
#                 print(prac[0])
#                 print(prac[1])
#                 result = prac[0] + prac[1]
#                 val = tokens.popleft()


#         return result
    
# check = Solution()

# tokens = [2,3,"+"]
# tokens = deque(tokens)

# ans = check.evalRPN(tokens)
# print(ans)

            
# Using research:
# URL: https://www.geeksforgeeks.org/python/evaluate-the-value-of-an-arithmetic-expression-in-reverse-polish-notation-in-python/

class Solution(object):
    def evalRPN(self, tokens):
        
        stack = []
        operands = ["+","-","*","/"] 

        for token in tokens:
            token = token.replace('\u2013', '-').replace('\u2014', '-')
            if token not in operands:
                stack.append(int(token))
            else:
                # Lifo
                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                elif token == "/":
                    stack.append(int(float(left) / right))

        return stack.pop()
    
check = Solution()

#tokens = [2,3,"+"] # case 1
#tokens = ["2","3","+"] # case 1.1
#tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"] #case 2
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] # case 3

tokens = deque(tokens)

ans = check.evalRPN(tokens)
print(ans)

# Notes:
# I messed up, on the left / right on else I had them switchted up and was getting a wrong answer. After that it was fixed. I need to remember that for next time. 