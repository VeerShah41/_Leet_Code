class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s=="":
            return True
        l = 0
        for i in t:
            if i==s[l]:
                l+=1
            if len(s)==l:
                return True
        return False