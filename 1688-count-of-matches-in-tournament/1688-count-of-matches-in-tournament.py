class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        matches = 0
        while n>0:
            matches+= (n%2) + (n//2)
            n=n//2
        return matches-1
