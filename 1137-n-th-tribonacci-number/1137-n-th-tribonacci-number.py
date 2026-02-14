class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        a=0
        b=1
        c=1
        for i in range(2,n):
            a,b,c=b,c,a+b+c
        return c
        
