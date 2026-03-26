class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        s=''
        z = columnNumber
        while z>0:

            y = z % 26
            if y==0:
                s=chr(64+26)+s
                z-=26
            else:
                s=chr(64+y)+s
                z-=y
            z = z // 26
            
            
            

        
        return s