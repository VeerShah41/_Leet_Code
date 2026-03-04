class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo={}
        def helper(i,j):
            if i>=j:
                if i==j:
                    return 1
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i]==s[j]:
                memo[(i,j)]=2+helper(i+1,j-1)
            else:
                memo[(i,j)]=max(helper(i+1,j),helper(i,j-1))
            return memo[(i,j)]
        return helper(0,len(s)-1)