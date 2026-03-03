class Solution(object):
    def buildArray(self, target, n):
        
        word_stack = []
        count = 0

        for i in range(1,n+1):

            if i in target:
                word_stack.append("Push")
                count += 1
                if count == len(target):
                    break
            else:
                word_stack.append("Push")
                word_stack.append("Pop")
            
        return word_stack



            

        