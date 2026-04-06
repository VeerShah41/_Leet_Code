class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n==1:
            return True
        x=n
        
        while x>1 :
            if x%2==0:
                x=x/2
            else:
                return False
            
                
        
        

        return x==1