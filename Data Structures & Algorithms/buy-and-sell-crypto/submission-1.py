class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        sell = prices[0]

        for p in prices:
            if p - sell > profit:
                profit = p - sell
            if sell > p:
                sell = p
        
        return profit