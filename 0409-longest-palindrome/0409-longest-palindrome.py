class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        f = {}
        for i in s:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        ans = 0
        
        for j in f.values():
            ans += (j//2)*2
        if ans<len(s):
            ans+=1

        return ans
