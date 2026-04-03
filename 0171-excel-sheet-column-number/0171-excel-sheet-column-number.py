class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        alpha = 26
        
        ans = ord(columnTitle[-1])-64
        i = len(columnTitle)-2
        while i>=0:
            x = ord(columnTitle[i])-64
            ans += (x*alpha)
            alpha*=26
            
            i-=1
            
        return ans