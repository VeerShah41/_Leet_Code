class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        w = n // 7
        d = n % 7

        f = w * 28 + 7 * (w * (w - 1) // 2)
        r = d * (w + 1) + d * (d - 1) // 2

        return f + r
     


