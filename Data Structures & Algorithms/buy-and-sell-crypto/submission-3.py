class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        highest = len(prices) - 1

        for i in range(len(prices) - 1, -1, -1):
            if prices[highest] < prices[i]:
                highest = i
            max_price = max(max_price, prices[highest] - prices[i])
        return max_price

        
        