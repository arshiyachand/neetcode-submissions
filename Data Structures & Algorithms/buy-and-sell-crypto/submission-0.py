class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        purchaseprice = prices[0]
        profit = 0

        for price in prices[1:]:
            if price < purchaseprice:
                purchaseprice = price
            else:
                profit = max(profit, price - purchaseprice)
        return profit


        