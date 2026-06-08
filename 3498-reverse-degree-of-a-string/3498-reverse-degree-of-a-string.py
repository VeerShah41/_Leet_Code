class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = 0
        for i in range(len(s)):
            
            p += ((i+1)*(26-(ord(s[i])-ord("a"))))
        return p