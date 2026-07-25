class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        one = float("-inf")
        sec = float("-inf")
        while n > 0:
            x = n%10
            if one<x:
                sec = one
                one=x
            elif sec<x:
                sec=x
            
            n//=10
        return one*sec