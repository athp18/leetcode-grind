class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if sorted(prices, reverse=True) == prices:
            return 0 #no profitable possible transactions, quick check
        max_profit = 0
        min_value = 1000000
        for price in prices:
            if price < min_value:
                min_value = price
            else:
                current_profit = price - min_value
                if current_profit > max_profit:
                    max_profit = current_profit
        return max_profit
