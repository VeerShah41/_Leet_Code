class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        squareSum = 0
        digitSum = 0
        while n>0:
            x=n%10
            squareSum+=(x**2)
            digitSum+=x
            n=n//10
        return (squareSum-digitSum)>=50


        