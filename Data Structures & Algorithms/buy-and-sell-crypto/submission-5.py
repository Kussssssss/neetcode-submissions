class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            margin = prices[r] - prices[l]
            
            if margin < 0:
                l = r
                r += 1
            else:
                r += 1

            profit = max(profit, margin)
            
        return profit
