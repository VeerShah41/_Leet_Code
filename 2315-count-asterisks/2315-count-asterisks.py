class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        inner = True
        ans = 0
        for i in s:
            if i=="|":
                inner = not inner
            elif i=="*" and inner:
                ans+=1
        return ans


        