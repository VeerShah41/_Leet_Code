class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float("inf")
        max_price = 0
        for price in prices:
            if min_price > price:
                min_price = price
            max_price = max(max_price,price-min_price)
        return max_price