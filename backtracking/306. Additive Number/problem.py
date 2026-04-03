
# Trial Version
from collections import deque

# class Solution(object):
#     def isAdditiveNumber(self, num):
        
#         stack = deque(num)

#         A = int(stack.popleft())
#         while stack:
            
#             B = int(stack.popleft())
#             if stack: C = int(stack.popleft())
#             else: 
#                 print(stack)
#                 return True

#             if A + B == C:
#                 A = C
#             else:
#                 print( A, B, C)
#                 return False
#         return True


class Solution(object):
    def isAdditiveNumber(self, num):
        
        for i in range(1, len(num) - 1):
            for j in range(i + 1, len(num)):
                a = int(num[0:i])
                b = int(num[i:j])
                remaining = num[j:]
                
                while remaining:
                    c = a + b
                    if not remaining.startswith(str(c)):
                        break
                    remaining = remaining[len(str(c)):]
                    a = b
                    b = c
                else:
                    return True
        return False
                






workit = Solution()

prints = workit.isAdditiveNumber("112358")

print(prints)
        