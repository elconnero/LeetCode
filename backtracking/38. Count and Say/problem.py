class Solution(object):
    
    def countAndSay(self, n): #if n = 3
        
        for i in range(1,n+1): #from 1 - 3

            if i == 1: #since i starts out i starts with this.
                word_output = "1"

            if i != 1 and i <= n: #Starting at 2 we bring it in here for recursiveness until we reach n.
                count = 1 #I am pretty sure we are going to need this count. 
                new_word = ""
                for j in range(len(word_output)): #So for this, j in range of the length of the wordcount. So from 0 tp whatever that wordcount will be. 

                    
                    if j < len(word_output)-1 and word_output[j] == word_output[j+1]: #so word_output[0] = "1" and if word_output[1] = "1" then we count it. 
                        count +=1
                    else: #If we do not get a freq up then we take the word_output add it's count then what we are working with. 
                        new_word = new_word + str(count) + word_output[j] 
                        count = 1
                word_output = new_word
        return word_output
                    

test = Solution()

word = test.countAndSay(4)
print(word)


