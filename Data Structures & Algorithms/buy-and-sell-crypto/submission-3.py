class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        if len(prices) == 1:
            return 0
        profit = 0
        buypointer = 0
        sellpointer = 1
        profit = prices[sellpointer] - prices[buypointer]

        while sellpointer < len(prices)-1:            
            if prices[sellpointer] < prices[buypointer]:
                buypointer = sellpointer
                sellpointer += 1
            else:
                sellpointer += 1
            profit = max( profit, prices[sellpointer] - prices[buypointer])
                

        return profit if profit > 0 else 0