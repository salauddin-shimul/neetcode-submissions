class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right = right + 1
            else:
                max_price = max(-prices[left] + prices[right], max_price)
                right += 1
        return max_price
