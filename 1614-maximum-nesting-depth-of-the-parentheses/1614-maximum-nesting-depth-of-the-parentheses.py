class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 0
        ans = 0
        for i in s:
            if i == "(":
                c+=1
            if i == ")":
                c-=1
            ans = max(ans,c)
        return ans