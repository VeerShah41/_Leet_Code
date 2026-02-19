import math
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        if dividend>=0 and divisor>0:

            return dividend//divisor
        else:
            if dividend<0 and divisor<0:
                return (abs(dividend)//abs(divisor))
            return (abs(dividend)//abs(divisor))*-1

        