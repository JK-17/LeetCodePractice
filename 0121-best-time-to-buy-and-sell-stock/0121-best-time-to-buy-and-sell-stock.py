class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        res = 0
        if len(prices) <= 1: return res

        while sell < len(prices):

            if prices[buy] > prices[sell]:
                buy = sell
                sell = buy+1
            else:
                res = max(prices[sell] - prices[buy], res)
                sell += 1
                
        return res