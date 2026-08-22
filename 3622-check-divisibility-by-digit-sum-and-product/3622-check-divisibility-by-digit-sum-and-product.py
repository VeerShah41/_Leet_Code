class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        p = 1
        s = 0 
        nn = n
        while nn>0:
            
            p*=nn%10
            s+=nn%10
            nn//=10
        return n%(p+s)==0

