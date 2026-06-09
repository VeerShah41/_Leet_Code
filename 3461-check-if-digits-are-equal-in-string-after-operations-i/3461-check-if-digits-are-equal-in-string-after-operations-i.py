class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = s
        while len(ans)>2:
            new = ''
            for i in range(len(ans)-1):
                new += str((int(ans[i]) + int(ans[i + 1])) % 10)
            ans = new
        return ans[0]==ans[1]
