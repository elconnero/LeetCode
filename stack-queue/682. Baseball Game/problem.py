class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        sum_stack = []
        for element in operations:
            if element.lstrip('-').isdigit(): 
                sum_stack.append(int(element))
            if (element == 'C') and sum_stack:
                sum_stack.pop()
            if (element == 'D') and sum_stack:
                sum_stack.append(sum_stack[-1]*2)
            if (element == '+') and len(sum_stack)>=2:
                sum_stack.append(sum_stack[-1]+sum_stack[-2])

        return sum(sum_stack)

sol = Solution()
print(sol.calPoints(["5","2","C","D","+"])) # expected 30
print(sol.calPoints(["1","C"])) # expected 0
print(sol.calPoints(["-3","5","D"])) # expected 12
print(sol.calPoints(["1","2","+","D"])) # expected 18
                    #1,2,3,6 = 12