
# class Solution(object):
#     def isValid(self, s):
        
#         opens = ["(","[","{"]
#         close = [")","]","}"]
#         other_stack = []

#         stack = list(s)

#         for elements in stack:
            
#             right_token = stack.pop()
#             if right_token in close:
#                 closer_index = close.index(right_token)
#                 left_token = stack.pop()
#                 if left_token in opens:
#                     opener_index = opens.index(left_token)

#                     if opener_index == closer_index: 

#                         if not stack: 
#                             return True
#                         else: 
#                             continue
#                     elif closer_index != opener_index:
                        
#                         for remaining_elements in stack:

#                             if not stack:
#                                 return False

#                             final_check = stack.pop()
                            
#                             if final_check in close:
#                                 return False
#                             else:
#                                 other_stack.append(final_check)
                        
#                         stack = stack + other_stack
#                     else: return False
#                 else: return False
#             else: return False

# class Solution(object):
#     def isValid(self, s):
        
#         opens = ["(","[","{"]
#         close = [")","]","}"]
#         stack = [None]
        
#         for tokens in s:
#             if tokens in opens:
#                 stack.append(tokens)
#             elif tokens in close:
#                 popped = stack.pop()
#                 opens_index = opens.index(popped)
#                 close_index = close.index(tokens)
#                 if opens_index == close_index:
#                     continue
#                 else:
#                     return False
#             else: return False
#         if stack: return False
#         else: return True
            

class Solution(object):
    def isValid(self, s):
        
        opens = ["(","[","{"]
        close = [")","]","}"]
        stack = []
        
        for tokens in s:
            if tokens in opens:
                stack.append(tokens)
            elif tokens in close:
                if not stack:
                    return False
                popped = stack.pop()
                opens_index = opens.index(popped)
                close_index = close.index(tokens)
                if opens_index == close_index:
                    continue
                else:
                    return False
            else: 
                return False
        if stack: 
            return False
        else: 
            return True


                        


test = Solution()

printer = test.isValid("]")

print(printer)








        