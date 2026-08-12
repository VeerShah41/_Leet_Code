class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = 1
        s = 0
        while n>0:
            x =n%10
            p*=(x)
            s+=x
            n//=10
        return p-s