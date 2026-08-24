class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 0
        c = x
        while c:
            s+=c%10
            c//=10
        if x%s==0:
            return s
        else:
            return -1