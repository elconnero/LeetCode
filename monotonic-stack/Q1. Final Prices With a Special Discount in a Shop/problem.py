# My way

class Solution(object):
    def finalPrices(self, prices):

        ans = []
        for i in range(len(prices)):
            if i <= len(prices):
                for j in range(len(prices)):
                    if (i < j) and (prices[i] >= prices[j]):
                        ans.append(prices[i]-prices[j])
                        break
                    elif j == len(prices)-1: ans.append(prices[i]) 
                    else: continue
                        
        return ans
                    
            
work = Solution()
prices = [8, 4, 6, 2, 3]
printME= work.finalPrices(prices)
print(printME)


        