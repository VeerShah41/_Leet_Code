class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        place = 1
        pro = 0
        s = 0
        while n>0:
            digit = n%10
            s+=digit
            if digit!=0:
                pro+=place*digit
                place*=10
            n//=10
        return pro*s