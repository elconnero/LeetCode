class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 1: return 0
        
        buy = prices[0]
        max_profit = 0

        for price in prices:

            if price < buy: buy = price
            if max_profit < price - buy: max_profit = price - buy
        return max_profit


            
            
            
        
        



sol = Solution()

test_cases = [
    [7, 1, 5, 3, 6, 4],   # 5  (buy at 1, sell at 6)
    [7, 6, 4, 3, 1],       # 0  (prices only go down, no profit)
    [1],                   # 0  (only one price, can't trade)
    [1, 2],                # 1  (buy at 1, sell at 2)
    [2, 1],                # 0  (can't sell before buying)
    [3, 3, 3, 3],          # 0  (all same price)
    [1, 2, 3, 4, 5],       # 4  (buy at 1, sell at 5)
]

for arr in test_cases:
    output = sol.maxProfit(arr)
    print(output, " ", arr)