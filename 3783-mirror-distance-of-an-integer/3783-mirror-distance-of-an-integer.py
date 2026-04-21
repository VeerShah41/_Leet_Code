class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = str(n)
        return abs(n-int(x[::-1]))
