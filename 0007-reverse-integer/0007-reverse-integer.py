class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=1
        if x<0:
            sign = -1
        x=abs(x)
        x=str(x)
        y= int(x[::-1])*sign
        if y<-2**31 or y>2**31-1:
            return 0
        return y