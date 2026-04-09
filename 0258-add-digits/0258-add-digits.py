class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        z=num
        if z<10:
            return int(z)
        while z>=10:
            s=0
            for i in str(z):
                s+=int(i)
            
            z = s
        return z