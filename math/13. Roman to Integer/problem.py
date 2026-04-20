from collections import deque

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = deque(s)
        value = 0

        while stack:
            element = stack.popleft()
            
            if   element == 'M': value += 1000
            elif element == 'D': value +=  500
            elif element == 'C': 
                if stack and stack[0] == 'M': 
                    stack.popleft()
                    value += 900
                elif stack and stack[0] == 'D': 
                    stack.popleft()
                    value += 400
                else: value += 100
            elif element == 'L': value +=   50
            elif element == 'X': 
                if stack and stack[0] == 'C': 
                    stack.popleft()
                    value += 90
                elif stack and stack[0] == 'L': 
                    stack.popleft()
                    value += 40
                else: value += 10
            elif element == 'V': value +=    5
            elif element == 'I': 
                if stack:
                    if stack[0] == 'X': 
                        stack.popleft()
                        value += 9
                    elif stack[0] == 'V': 
                        stack.popleft()
                        value += 4
                    else: value += 1
                else: value += 1
            else: continue
        
        return value
    
test = Solution()
vales = ["III", "LVIII", "MCM", "MCMXCIV"]

for i in range(len(vales)): print(test.romanToInt(vales[i]))

"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        r = 0
        for i in range(len(s)):
            if i < len(s) - 1 and v[s[i]] < v[s[i+1]]:
                r -= v[s[i]] 
            else:
                r += v[s[i]]
        return r
# This is the way better way. 
"""